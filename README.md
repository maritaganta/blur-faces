# Face Detection and Blurring with OpenCV

This project demonstrates how to perform face detection and apply a significant blur to detected faces using OpenCV in Python. The application uses a webcam feed to detect faces in real-time and blurs them for privacy.

## Prerequisites

- Python 3.x
- OpenCV

## Usage

1. **Run the Application:**:
   ```bash
   python main.py

2. **Functionalities:**:
* The application captures video from the default webcam.
* It detects faces using a pre-trained Haar cascade classifier.
* Detected faces are blurred using a Gaussian blur with a large kernel size.

3. **Controls:**:
* Press q to quit the application.

## TODO
* Add tracking to the faces
* Add prediction filter to the detections
* Do not blur known faces: Implement a method to identify known faces using a facial recognition system and exclude them from blurring.
* Blur out text: Detect and blur text within the video frames, ensuring privacy and preventing information leakage.


