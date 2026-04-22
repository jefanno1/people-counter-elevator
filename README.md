# 🧠 People Counter Application
The People Counter Application is a computer vision-based project designed to track and count individuals in a video stream. It utilizes object detection and tracking algorithms to provide accurate counts of people moving through predefined regions of interest. This application has numerous potential use cases, including surveillance, crowd management, and traffic analysis.

## 🎬 Demo

![People Counter Demo](./detection/people_counter_result.gif)

## 🚀 Features
- **Object Detection:** Detects people in video frames using the YOLO model.
- **Tracking:** Tracks the movement of detected individuals across frames.
- **Masking and Region of Interest (ROI):** Applies a mask to focus on a specific area of the video frames.
- **Counting Logic:** Maintains counters for individuals moving through predefined limits.
- **Output and Visualization:** Writes the processed video with annotations to a new video file.

## 🛠️ Tech Stack
* OpenCV (`cv2`) for video capture, frame processing, and visualization
* NumPy (`np`) for numerical computations
* cvzone for additional computer vision functionalities
* ultralytics for loading and utilizing the YOLO model
* CSV and OS for logging and file system operations

## 📦 Installation
To install the required dependencies, run the following command:
```bash
pip install opencv-python numpy cvzone ultralytics
```
Ensure you have the necessary video files (`people.mp4`, `mask.png`) and the YOLO model (`yolov8n.pt`) in the correct directories.

Link to download resource : https://drive.google.com/drive/folders/1ZDJZdV03lZNdnx8huZ8UW--M6l_rsiaU?usp=sharing

## 📁Project Structure
```markdown
people-counter-elevator/
│
├── detection/
│   └── person_tracker_result.mp4
│
├── source/
│   └── people.mp4
│
├── model/
│   └── yolov8n.pt
├── mask.png
├── people_counter_main.py
└── requirements.txt
```

## 💻 Usage
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `people_counter_main.py` script using Python:
```bash
python people_counter_main.py
```
This will start the people counting application, and the processed video will be saved to a new file (`person_tracker_result.mp4`).


## 🤝 Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## 📝 License
This project is licensed under the MIT License.

## 📬 Contact
For any questions or concerns, please don't hesitate to reach out to us.
