# ScreenshotOfYoutubeUrl 

This is a Python script that downloads a YouTube video and extracts frames from it. The extracted frames are then saved as images and renamed with a specified prefix.

## Requirements

- Python 3.x
- `pytube` library

## Installation

1. Clone the repository:
git clone https://github.com/Yushirizu/ScreenshotOfYoutubeUrl


2. Install the `pytube` library:

$ pip install pytube


## Usage

1. Open the `download.py` file and replace the `youtube_url` and `output_path` variables with the URL of the YouTube video you want to download and the directory where you want to save the downloaded video, respectively.

2. Run the `download.py` file to download the YouTube video.

3. Open the `extract.py` file and replace the `video_filename`, `crop_width`, `crop_height`, and `image_prefix` variables with the filename of the downloaded video, the width and height of the cropped frames, and the prefix to be added to the filenames of the extracted images, respectively.

4. Run the `extract.py` file to extract frames from the downloaded video and save them as images.

5. Open the `rename.py` file and replace the `directory_path` and `image_prefix` variables with the directory where the extracted images are located and the prefix to be added to the filenames of the images, respectively.

6. Run the `rename.py` file to rename the extracted images.
