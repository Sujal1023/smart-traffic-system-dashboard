import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # Ensure you have 'yolov8n.pt' or replace it with your model path

# Load the image
image_path = 'Image Files/traffic.jpg'  # Replace with your image file path
original_image = cv2.imread(image_path)

# Perform inference
results = model(original_image)

# Get bounding boxes and class IDs
boxes = results[0].boxes.xyxy  # Bounding box coordinates (x1, y1, x2, y2)
classes = results[0].boxes.cls  # Class IDs

# Define vehicle class IDs (COCO classes: 2-car, 5-bus, 7-truck)
vehicle_classes = [2, 5, 7]

# Copy the original image for annotation
annotated_image = original_image.copy()

# Draw bounding boxes without confidence numbers
detected_vehicles = 0
for box, cls in zip(boxes, classes):
    if int(cls) in vehicle_classes:
        x1, y1, x2, y2 = map(int, box)  # Convert coordinates to integers
        color = (0, 255, 0)  # Green bounding box color
        cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, 2)
        detected_vehicles += 1  # Count detected vehicles

# Display detected vehicle count on the annotated image
cv2.putText(annotated_image, f'Detected Vehicles: {detected_vehicles}', (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Stack images horizontally for comparison
comparison_image = np.hstack((original_image, annotated_image))

# Display the comparison image
while True:
    cv2.imshow('Vehicle Detection Comparison', comparison_image)

    # Wait for a key event
    key = cv2.waitKey(1) & 0xFF

    # Press 'b' for Back or 'q' to quit
    if key == ord('b'):
        print("Back button pressed, returning to the main menu...")
        break  # Exit the loop to return to the main program or call another function
    elif key == ord('q'):
        print("Exiting the application...")
        cv2.destroyAllWindows()
        exit()  # Close the program completely

# Clean up windows
cv2.destroyAllWindows()
