import os
from ultralytics import YOLO
import cv2

# Get the current directory
CURRENT_DIR = os.getcwd()

# Load the YOLO model
MODEL = os.path.join(CURRENT_DIR, 'models', 'best.pt')
model = YOLO(MODEL)

# Open the webcam (use 0 for the default camera)
CAPTURE = cv2.VideoCapture(0)

# Check if the camera was successfully opened
if not CAPTURE.isOpened():
    print("Error: Unable to access the webcam.")
    exit()

# Process the video frame by frame
while True:
    ret, frame = CAPTURE.read()
    if not ret:
        print("Failed to capture frame")
        break  # Exit when the video ends or there's an issue with the frame

    # Perform YOLO detection on the current frame
    results = model.predict(source=frame, save=False)  # Predict without saving results
    annotated_frame = results[0].plot()  # Get the annotated frame with detections

    # Display the annotated frame in a window
    cv2.imshow("Webcam Detection", annotated_frame)

    # Exit on pressing the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture resources and close the display window
CAPTURE.release()
cv2.destroyAllWindows()