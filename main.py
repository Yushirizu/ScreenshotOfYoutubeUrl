import cv2
import os
import random
import threading
import subprocess

# --- Constants ---
VIDEO_OUTPUT_DIR = "Video"
IMAGE_OUTPUT_DIR = "Baldy_Images"
IMAGE_PREFIX = "Baldy"
NUM_IMAGES_TO_EXTRACT = 100
YOUTUBE_URL = "https://youtu.be/i8IHxxCPP5E?si=7mBNAVV4OulPEXoa"


def download_youtube_video(youtube_url, output_dir):
    """Download a YouTube video using yt-dlp."""
    os.makedirs(output_dir, exist_ok=True)
    command = [
        "yt-dlp",
        "-o", os.path.join(output_dir, "%(title)s.%(ext)s"),
        "-f", "bestvideo[codec!=av01][ext=mp4]+bestaudio[ext=m4a]/mp4",
        "--merge-output-format", "mp4",
        youtube_url
    ]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        return next((os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".mp4")), None)
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None


def get_random_frame(video_filename, timestamp_sec):
    """Extract a frame from the video at a specific timestamp."""
    cap = cv2.VideoCapture(video_filename)
    if not cap.isOpened():
        print(f"Error: Could not open video file: {video_filename}")
        return None
    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp_sec * 1000)
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None


def get_user_crop(video_filename):
    """Allow the user to select a cropping rectangle from a slideshow of 3 frames."""
    for _ in range(3):
        timestamp = random.uniform(0, 10)
        frame = get_random_frame(video_filename, timestamp)
        if frame is None:
            print(f"Error: Could not retrieve a frame at {timestamp:.2f}s.")
            continue

        print("Displaying a frame for cropping. Select a region and press ENTER.")
        x, y, w, h = cv2.selectROI("Select Crop Area", frame, fromCenter=False, showCrosshair=True)
        cv2.destroyAllWindows()

        if w > 0 and h > 0:
            print(f"Selected crop area: x={x}, y={y}, width={w}, height={h}")
            return x, y, w, h

    print("No suitable cropping area selected after 3 attempts. Exiting.")
    return None


def save_cropped_frame(video_filename, crop_area, timestamp, output_path):
    """Extract, crop, and save a frame."""
    frame = get_random_frame(video_filename, timestamp)
    if frame is not None:
        x, y, w, h = crop_area
        cropped = frame[y:y + h, x:x + w]
        cv2.imwrite(output_path, cropped)


def rename_images(directory, prefix):
    """Rename images sequentially."""
    for i, file in enumerate(sorted(f for f in os.listdir(directory) if f.endswith(".jpg")), 1):
        os.rename(os.path.join(directory, file), os.path.join(directory, f"{prefix}_{i:04d}.jpg"))


def main():
    video_path = download_youtube_video(YOUTUBE_URL, VIDEO_OUTPUT_DIR)
    if not video_path:
        print("Failed to download video.")
        return

    crop_area = get_user_crop(video_path)
    if not crop_area:
        print("No cropping area selected. Exiting.")
        return

    cap = cv2.VideoCapture(video_path)
    duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / (cap.get(cv2.CAP_PROP_FPS) or 30)
    cap.release()

    os.makedirs(IMAGE_OUTPUT_DIR, exist_ok=True)
    threads = [
        threading.Thread(
            target=save_cropped_frame,
            args=(video_path, crop_area, random.uniform(0, duration), os.path.join(IMAGE_OUTPUT_DIR, f"{IMAGE_PREFIX}_temp_{i}.jpg"))
        )
        for i in range(NUM_IMAGES_TO_EXTRACT)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    rename_images(IMAGE_OUTPUT_DIR, IMAGE_PREFIX)
    print("Process completed.")


if __name__ == "__main__":
    main()