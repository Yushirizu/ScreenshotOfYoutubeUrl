## Setup and Usage

This guide assumes you have Python 3.6+ installed.

1.  **Clone the repo**

2.  **Set up Python Environment:**
    *   Open terminal/command prompt in the script's directory.
    *   Create a virtual environment:
        ```bash
        python3 -m venv .venv
        ```
    *   Activate the environment:
        *   macOS/Linux: `source .venv/bin/activate`
        *   Windows: `.venv\Scripts\activate`
    *   Install required Python packages:
        ```bash
        pip install opencv-python
        pip install yt-dlp
        ```

3.  **Run the Script:**
    *   With the virtual environment activated, run:
        ```bash
        python3 main.py
        ```

4.  **Process Flow:**
    *   The script downloads the video (specified by `YOUTUBE_URL`).
    *   A window titled "Select Crop Area" will appear showing a video frame.
    *   **Click and drag** a rectangle over the area you want to crop from future frames.
    *   Press **Enter** to confirm your selection. (Press **Esc** to try a different frame if needed).
    *   The script will then automatically extract, crop, and save the specified number of random frames in the `Baldy_Images` directory, named `Baldy_0001.jpg`, etc.

## Output

*   Downloaded video is saved in the `Video` directory.
*   Cropped images are saved in the `Baldy_Images` directory, sequentially named.

## Customization

Edit the constants at the top of `frame_extractor.py` to change the video URL, output directories, file prefix, and the number of images to extract:

```python
# --- Constants ---
VIDEO_OUTPUT_DIR = "Video"
IMAGE_OUTPUT_DIR = "Baldy_Images"
IMAGE_PREFIX = "Baldy"
NUM_IMAGES_TO_EXTRACT = 100
YOUTUBE_URL = "https://youtu.be/i8IHxxCPP5E?si=7mBNAVV4OulPEXoa"
```
