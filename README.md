# Smart-traffic-system-dashboard
<img width="801" alt="Screenshot 2024-12-09 at 8 24 16 PM" src="https://github.com/user-attachments/assets/ea9a7e9c-6ccc-493e-a61b-38285f4a935b">

Smart Traffic System Manager

This project demonstrates the use of YOLOv8 (You Only Look Once, version 8) for vehicle detection in images. It includes functionality to detect specific vehicle classes (cars, buses, trucks), count the detected vehicles, and visualize the results.

Features

Object Detection: Identifies and draws bounding boxes around vehicles in the image.

Vehicle Count: Counts the number of detected vehicles belonging to specific classes.

Comparison Visualization: Displays the original image alongside the annotated image for comparison.

Customizable Classes: Allows detection of specific classes of interest (e.g., cars, buses, trucks).

Tech Stack

Programming Language: Python

Libraries: OpenCV, NumPy, YOLOv8

Installation

Prerequisites

Python 3.8 or above.

Virtual environment (recommended).

Image file for testing (e.g., traffic.jpg).

Setup

Clone the repository:

git clone https://github.com/yourusername/vehicle-detection-yolov8.git
cd vehicle-detection-yolov8

Install dependencies:

pip install -r requirements.txt

Ensure ultralytics, opencv-python, and numpy are included in the requirements.txt file.

Download YOLOv8 model weights:

wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt

Alternatively, replace yolov8n.pt with the path to your preferred YOLOv8 model.

Usage

Place your image file in the Image Files directory (or adjust the file path in the script).

Run the Python script:

python vehicle_detection.py

Interact with the display:

Press 'b': Return to the main menu or stop the visualization loop.

Press 'q': Quit the application entirely.

File Structure

vehicle-detection-yolov8/
├── Image Files/
│   └── traffic.jpg        # Example input image
├── vehicle_detection.py   # Main script for vehicle detection
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation

Example Output

After running the script, a window will display:

The original image on the left.

The annotated image with bounding boxes and the vehicle count on the right.

Sample Screenshot

(Replace with an actual screenshot of the comparison output)

Key Functions

generate_random_traffic_data

Generates synthetic traffic data for simulation purposes.

update_traffic_data

Fetches traffic data and updates the display accordingly.

set_signal

Manages traffic signal states for each lane (red, yellow, green).

Customization

Modify Detected Classes

To detect additional classes, edit the vehicle_classes list in the script:

vehicle_classes = [2, 5, 7]  # COCO class IDs: 2-car, 5-bus, 7-truck

Replace the class IDs with those relevant to your application.

Adjust Visualization

Change bounding box colors or overlay text properties using OpenCV functions in the vehicle_detection.py file.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch:

git checkout -b feature-name

Commit your changes:

git commit -m "Add feature description"

Push to your branch:

git push origin feature-name

Submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Ultralytics for the YOLOv8 framework.

OpenCV and NumPy for image processing and mathematical operations.

Contact

For questions or feedback, feel free to reach out:

Email: sujalchoudhary1023@gmail.com

GitHub: Sujal1023

Thank you for exploring the Smart Traffic System Manager project!
