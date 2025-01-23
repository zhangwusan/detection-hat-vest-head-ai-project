import os
from ultralytics import YOLO
import cv2

# Get the current directory
CURRENT_DIR = os.getcwd()

# Load the YOLO model
MODEL = os.path.join(CURRENT_DIR, 'models', 'best.pt')
model = YOLO(MODEL)

YES_OPTION = ['Y', 'YES']

OPTION = input('Do you want to input video? (Yes/No) : ')

if OPTION.upper() in YES_OPTION:
    video = input('Please enter video path: ')
    VIDEO_PATH = os.path.join(CURRENT_DIR, video)
else: 
    VIDEO_PATH = os.path.join(CURRENT_DIR, 'downloads', 'The Power and Beauty of Construction Sites： A Cinematic Reel.mp4')

CAPTURE = cv2.VideoCapture(VIDEO_PATH)

# Check if the video was successfully opened
if not CAPTURE.isOpened():
    print("Error: Unable to open video file.")
    exit()

# Process the video frame by frame
while True:
    ret, frame = CAPTURE.read()
    if not ret:
        break 

    # Perform YOLO detection on the current frame
    results = model.predict(source=frame, save=False)
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("Video Detection", annotated_frame)

    # Exit on pressing the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video resources
CAPTURE.release()
cv2.destroyAllWindows()