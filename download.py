from pytube import YouTube


def download_youtube_video(youtube_url, output_path):
    try:
        yt = YouTube(youtube_url)
        video_stream = yt.streams.filter(
            file_extension="mp4", progressive=False).order_by('resolution').desc().first()
        video_stream.download(output_path)
        return video_stream.default_filename
    except Exception as e:
        print(f"Error downloading YouTube video: {e}")
        return None


def main():
    # Replace with the YouTube video URL
    youtube_url = "https://www.youtube.com/watch?v=5s-O3oluZJM"
    # Replace with the directory where you want to save the downloaded video
    output_path = "Video"
    video_filename = download_youtube_video(youtube_url, output_path)
    if video_filename:
        print(f"Video downloaded successfully: {video_filename}")


if __name__ == "__main__":
    main()
