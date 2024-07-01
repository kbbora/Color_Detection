# Color Detection Application

This Python application uses OpenCV and other Python libraries to detect and classify objects by their colors in real-time video captured from a webcam. It has a user-friendly interface that allows for real-time color-based object classification and counting as they cross a defined line.

## Features

- Real-time video capture using a webcam
- Color-based object detection and classification
- Counting objects as they cross a defined line
- User-friendly interface built with Tkinter

## Installation

To run this application, you need to have Python installed along with the following libraries:

- OpenCV
- NumPy
- Tkinter
- PIL (Python Imaging Library)

You can install the required libraries using pip:

```bash
pip install opencv-python numpy pillow
```
## Usage
1. Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/color-detection-application.git
cd color-detection-application
```
2. Run the application:
```bash
python app.py
```
3. The application will start and access your camera. Objects crossing a defined line will be detected and classified by their colors. The counts will be displayed in the application interface.
## How It Works
1. The application captures video from the webcam.
2. The captured frames are converted to the HSV color space for color detection.
3. Color masks are created for each target color.
4. Contours in the masked images are detected, and objects are identified.
5. When an object crosses a defined line, its color is classified, and the count is updated.
6. The interface displays the count of detected objects for each color and the total count.
## Configuration
By default, the following colors are detected: green, blue, red, yellow, orange, purple, and pink. Threshold settings for each color can be adjusted in the code.


## Contributing
Contributions are welcome! If you have any suggestions for improvements or if you want to report a bug, please open an issue or submit a pull request.


