# ✋ Hand Gesture Based LED Controller 💡

## 📌 Project Overview

The **Hand Gesture Based LED Controller** is a real-time computer vision and embedded systems project developed using Python and ESP32.

This project uses a webcam to detect hand gestures and count the number of raised fingers. The detected finger count is transmitted from Python to an ESP32 through serial communication.

The ESP32 processes the received data and controls five LEDs according to the detected finger count.

## 🚀 Features

- Real-time hand detection using a webcam
- Finger counting (0–5)
- Hand landmark detection and tracking
- Computer vision-based gesture recognition
- Serial communication between Python and ESP32
- Control of five LEDs using hand gestures
- Automatic LED updates when the finger count changes

## 🛠️ Technologies & Libraries

### Software & Libraries

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Real-time video capture and image processing |
| CVZone | Hand detection and finger tracking |
| MediaPipe | Hand landmark detection |
| PySerial | Serial communication between Python and ESP32 |

### Hardware Components

- ESP32 Development Board
- 5 LEDs
- 5 Current-Limiting Resistors
- Webcam
- USB Cable
- Jumper Wires

## ⚙️ Working Principle

1. The webcam captures real-time video.
2. OpenCV processes the video frames.
3. CVZone HandTrackingModule detects and tracks the hand.
4. MediaPipe identifies the hand landmarks.
5. Python calculates the total number of raised fingers.
6. The detected finger count is sent to the ESP32 through serial communication.
7. The ESP32 receives the finger count and controls the LEDs.

## 💡 LED Control Logic

The number of active LEDs depends on the number of raised fingers.

| Finger Count | LED 1 | LED 2 | LED 3 | LED 4 | LED 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | OFF | OFF | OFF | OFF | OFF |
| 1 | ON | OFF | OFF | OFF | OFF |
| 2 | ON | ON | OFF | OFF | OFF |
| 3 | ON | ON | ON | OFF | OFF |
| 4 | ON | ON | ON | ON | OFF |
| 5 | ON | ON | ON | ON | ON |

## 🔌 ESP32 Pin Configuration

| LED | ESP32 GPIO Pin |
|---|:---:|
| LED 1 | GPIO 2 |
| LED 2 | GPIO 0 |
| LED 3 | GPIO 17 |
| LED 4 | GPIO 18 |
| LED 5 | GPIO 21 |

## 📦 Installation

### 1. Install Python Libraries

Open your terminal and run:

```bash
pip install opencv-python cvzone mediapipe pyserial
```

### 2. Connect the Hardware

Connect five LEDs to the ESP32 using suitable current-limiting resistors.

### 3. Upload Arduino Code

Open the `led_controller.ino` file using Arduino IDE and upload it to your ESP32.

### 4. Configure Serial Port

Open the Python script and check the serial port configuration:

```python
ser = serial.Serial('COM3', 9600)
```

Change `COM3` according to your ESP32 serial port.

### 5. Run the Python Program

```bash
python hand_gesture_detection.py
```

Show your hand in front of the webcam and control the LEDs using finger gestures.

Press `ESC` to exit the application.

## 📁 Project Structure

```text
Hand-Gesture-Based-LED-Controller/
│
├── Python/
│   └── hand_gesture_detection.py
│
├── Arduino/
│   └── led_controller.ino
│
├── README.md
│
└── requirements.txt
```

## 🔮 Future Improvements

- Wireless communication between Python and ESP32
- Control multiple electrical devices
- Add more hand gestures for different commands
- Develop a smart home automation system

## 👨‍💻 Author

Developed as a Computer Vision and Embedded Systems project.

**Technologies:** Python | OpenCV | CVZone | MediaPipe | ESP32 | Arduino

---

⭐ If you find this project interesting, feel free to star the repository!