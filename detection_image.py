import os
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

# Get the current directory
CURRENT_DIR = os.getcwd()

# Load the model
MODEL = os.path.join(CURRENT_DIR, 'models', 'best.pt')
model = YOLO(MODEL)

# Predict on an image
IMAGE_PATH = os.path.join(CURRENT_DIR, 'images', 'testing.jpeg')
results = model.predict(IMAGE_PATH, save=False)  # Disable saving

# Read the original image using OpenCV
original_image = cv2.imread(IMAGE_PATH)
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)  # Convert to RGB for matplotlib

# Annotate the image with predictions
annotated_image = results[0].plot()  # Draw bounding boxes, labels, etc.

# Ensure consistent color representation by keeping both in RGB
annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

# Display the original and annotated images side by side
plt.figure(figsize=(15, 7))

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(original_image_rgb)
plt.axis('off')
plt.title("Original Image")

# Show the annotated image
plt.subplot(1, 2, 2)
plt.imshow(annotated_image_rgb)
plt.axis('off')
plt.title("Predicted Image with Detections")

# Display both images
plt.tight_layout()
plt.show()