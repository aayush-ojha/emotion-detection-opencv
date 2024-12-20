# Emotion Detection with OpenCV and DeepFace

This project uses OpenCV and DeepFace to detect emotions from webcam feed, video files, or image files.

## Requirements

- Python 3.x
- OpenCV
- DeepFace

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/aayush-ojha/emotion-detection-opencv.git
    cd emotion-detection-opencv
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script and follow the prompts to select the input source (webcam, video file, or image file):

```sh
python3 main.py
```

### Webcam

To use the webcam as the input source, enter `webcam` when prompted.

### Video File

To use a video file as the input source, enter the path to the video file when prompted. Supported formats include `.mp4`, `.avi`, and `.mov`.

### Image File

To use an image file as the input source, enter the path to the image file when prompted. Supported formats include `.jpg`, `.jpeg`, and `.png`.

## Example

```sh
Enter the source (webcam, video file path, or image file path): webcam
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.