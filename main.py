import cv2
import threading
import random


def get_random_timestamp(duration):
    # Generate a random timestamp within the duration of the video
    return random.uniform(0, duration)


def get_random_frame(video_filename, timestamp):
    # Open the video file
    cap = cv2.VideoCapture(video_filename)

    # Set the timestamp
    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)

    # Read the frame
    ret, frame = cap.read()

    # Release the video file
    cap.release()

    return frame


def crop_bottom_right(frame, width, height):
    # Get the dimensions of the frame
    frame_height, frame_width, _ = frame.shape

    # Crop the frame to the desired dimensions (bottom right)
    cropped_frame = frame[frame_height -
                          height:frame_height, frame_width-width:frame_width]

    return cropped_frame


def extract_and_save_image(video_filename, crop_width, crop_height, random_timestamp, image_filename):
    # Get a random frame from the video file
    frame = get_random_frame(video_filename, random_timestamp)

    # Crop the frame to the desired dimensions (bottom right)
    cropped_frame = crop_bottom_right(
        frame, width=crop_width, height=crop_height)

    # Save the cropped frame as an image
    cv2.imwrite(image_filename, cropped_frame)
    print(
        f"Saved random cropped image at timestamp: {random_timestamp} seconds")


def main():

    # Set the video file name and path
    video_filename = "GettingOverIt.mp4"

    # Open the video file
    cap = cv2.VideoCapture(video_filename)

    # Get the total number of frames and FPS of the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Set a default FPS value if it's zero
    if fps == 0:
        fps = 30  # You can change this value to any desired default FPS

    # Calculate the duration of the video
    duration = total_frames / fps

    # Set the number of images to extract
    num_images_to_extract = 100  # You can change this number as per your requirement

    # Set the crop dimensions
    crop_width = 344
    crop_height = 800

    # Extract and save the images using multi-threading
    threads = []
    for i in range(num_images_to_extract):
        image_filename = f"Nerissa_{i}.jpg"
        random_timestamp = get_random_timestamp(duration)
        t = threading.Thread(target=extract_and_save_image, args=(
            video_filename, crop_width, crop_height, random_timestamp, image_filename))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Release the video file
    cap.release()


if __name__ == "__main__":
    main()
