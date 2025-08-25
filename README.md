"""
# Face and Ghost Detector
  ![Preview](test.gif)
This is a Python application that uses OpenCV and the `cvzone` library to detect faces in a webcam feed and overlay a playful "ghost detector" feature. The program draws green rectangles around detected faces, displays attributes like age, mood, and gender, and simulates ghost detection with randomly positioned boxes.

## Features
- **Face Detection**: Detects faces in real-time using the `cvzone` FaceDetectionModule.
- **Attribute Display**: Shows hardcoded attributes (age, mood, gender) for detected faces.
- **Ghost Detector**: Simulates ghost detection by placing green boxes with fake attributes (age, mood, gender) at random positions.
- **Real-Time Processing**: Processes webcam feed and updates the display continuously.

## Prerequisites
- Python 3.6+
- OpenCV (`opencv-python`)
- cvzone (`cvzone`)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/face-ghost-detector.git
   cd face-ghost-detector ```
2. **Install dependencies**:
   ` pip install opencv-python cvzone `
3. **Code Overview**:

  # Libraries:
  
  cv2: OpenCV for image processing and webcam access.
  cvzone.FaceDetectionModule: For face detection.
  random: To position ghost boxes randomly.
  
  # Key Components:
  
  Face detection with FaceDetector (confidence threshold: 0.5).
  Hardcoded face attributes displayed below each face.
  Two "ghost" boxes that reposition every 45 frames with fake attributes.
  
  # Customization:
  
  Replace hardcoded attributes with an AI model for real attribute detection.
  Adjust minDetectionCon for face detection sensitivity.
  Modify ghosts list to change the number or size of ghost boxes.

4. **License**:
    This project is licensed under the MIT License. See the LICENSE file for details.
"""
