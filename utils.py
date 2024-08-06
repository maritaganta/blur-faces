import cv2
import numpy as np

def run():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi = frame[y:y+h, x:x+w]
            blurred_roi = cv2.GaussianBlur(roi, (201, 201), 0)  # (21, 21) is the kernel size, adjust as needed
            frame[y:y+h, x:x+w] = blurred_roi

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()