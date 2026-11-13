import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import time

# Arduino
ser = serial.Serial('COM3', 9600)
time.sleep(2)

# Camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.7, maxHands=1)

total_fingers = 0
prev_fingers = -1

while True:

    success, img = cap.read()

    if not success:
        break

    # Detect hand
    hands, img = detector.findHands(img)

    # Count fingers
    if len(hands) == 1:

        hand = hands[0]

        fingers = detector.fingersUp(hand)

        total_fingers = sum(fingers)

        print("Finger list:", fingers)
        print("Total fingers:", total_fingers)

    else:
        total_fingers = 0

    # Send Arduino only when number changes
    if total_fingers != prev_fingers:

        ser.write((str(total_fingers) + '\n').encode())

        print("Arduino:", total_fingers)

        prev_fingers = total_fingers

    # Show number
    cv2.putText(
        img,
        str(total_fingers),
        (128, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        4,
        (100, 50, 200),
        10
    )

    # Vertical lines
    # cv2.line(img, (128, 0), (128, img.shape[0]), (255, 0, 0), 2)
    # cv2.line(img, (256, 0), (256, img.shape[0]), (0, 255, 0), 2)
    # cv2.line(img, (384, 0), (384, img.shape[0]), (0, 0, 255), 2)
    #
    # # Horizontal lines
    # cv2.line(img, (0, 128), (img.shape[1], 128), (255, 0, 0), 2)
    # cv2.line(img, (0, 256), (img.shape[1], 256), (0, 255, 0), 2)
    # cv2.line(img, (0, 384), (img.shape[1], 384), (0, 0, 255), 2)

    # Show
    cv2.imshow("Light Controller", img)

    # ESC
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
#ser.close()