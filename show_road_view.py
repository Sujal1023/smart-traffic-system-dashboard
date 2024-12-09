import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO
import threading

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Replace with your YOLO model file


class MultiLaneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Lane Vehicle Counter")

        # Initialize variables
        self.video_frames = []
        self.caps = [None] * 4  # Four video sources
        self.running = [False] * 4

        # Create GUI layout
        for i in range(4):
            frame = tk.Frame(root, width=400, height=300, bg="black", relief=tk.SUNKEN, bd=2)
            frame.grid(row=i // 2, column=i % 2, padx=5, pady=5)
            canvas = tk.Canvas(frame, width=400, height=300, bg="black")
            canvas.pack()
            self.video_frames.append({"frame": frame, "canvas": canvas, "lane_counts": 0})

        # Buttons for each video
        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.video_frames[i]["frame"], text="Upload Video",
                            command=lambda idx=i: self.load_video(idx))
            btn.pack(side=tk.BOTTOM, pady=5)
            self.buttons.append(btn)

    def load_video(self, index):
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi")])
        if video_path:
            self.caps[index] = cv2.VideoCapture(video_path)
            self.running[index] = True
            threading.Thread(target=self.process_video, args=(index,)).start()

    def process_video(self, index):
        while self.running[index] and self.caps[index].isOpened():
            ret, frame = self.caps[index].read()
            if not ret:
                self.running[index] = False
                break

            # Resize frame
            frame = cv2.resize(frame, (400, 300))

            # Perform YOLO detection
            results = model(frame)
            vehicle_count = 0  # Total vehicles in this lane (frame)

            for box, conf, cls in zip(results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls):
                # Draw bounding boxes
                x1, y1, x2, y2 = map(int, box)  # Bounding box coordinates
                label = model.names[int(cls)]  # Class name
                confidence = f"{conf:.2f}"  # Confidence score

                # Filter only vehicles (optional: based on specific classes)
                if label in ["car", "truck", "bus"]:
                    vehicle_count += 1
                    # Draw bounding box and label
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} {confidence}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Annotate the frame with vehicle count
            cv2.putText(frame, f"Lane {index + 1}: {vehicle_count}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # Red color for count text

            # Convert BGR to RGB and display on canvas
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)

            self.video_frames[index]["canvas"].create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.video_frames[index]["canvas"].image = img_tk

        # Release video capture when done
        if self.caps[index]:
            self.caps[index].release()


# Initialize application
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiLaneApp(root)
    root.mainloop()
