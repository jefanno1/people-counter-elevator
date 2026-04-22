import cv2
import numpy as np
import cvzone
import csv
import os

from datetime import datetime
from collections import deque
from ultralytics import YOLO

# ----------------------------
# Check Dir
# ----------------------------
output_dir = r'.\detection'
output_file = os.path.join(output_dir, "person_tracker_result.mp4")
model_dir = r'.\model'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

counter_up = 0
counter_down = 0
person_id_collector = []
track_history = {}


mask = cv2.imread(r".\mask.png")
cap = cv2.VideoCapture(r".\source\people.mp4")
model = YOLO(r".\model\yolov8n.pt")

frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))


out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width,frame_height))

if not cap.isOpened():
    print("Video Error")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    limitsUp = [103, 161, 296, 161]
    limitsDown = [527, 489, 735, 489]
    cv2.line(frame, (limitsUp[0], limitsUp[1]), (limitsUp[2], limitsUp[3]), (0, 0, 255), 5)
    cv2.line(frame, (limitsDown[0], limitsDown[1]), (limitsDown[2], limitsDown[3]), (0, 0, 255), 5)

    if len(mask.shape) == 2:
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    imgRegion = cv2.bitwise_and(frame,mask)

    results = model.track(imgRegion,classes=[0],persist=True)[0]
    # annotated_frame = results.plot()
    for box in results.boxes:
        if box.id is not None:

            # Draw Rectangle
            person_id = int(box.id[0].cpu().numpy())
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 3)
            cvzone.putTextRect(frame, f"Person_ID : {person_id}", (int(x1), int(y1)-10), scale=1.5, thickness=3)

            # Draw Center
            cx, cy, w, h = box.xywh[0].cpu().numpy()
            cx = int(cx)
            cy = int(cy)
            center = (int(cx), int(cy))
            cv2.circle(frame, center, 3, (255, 0, 0), -1)


            # Trails
            if person_id not in track_history:
                track_history[person_id] = deque(maxlen=30)
            track_history[person_id].append(center)


            # Draw the trails
            if len(track_history[person_id]) > 1:
                points = np.array(track_history[person_id], np.int32).reshape((-1,1,2))
                cv2.polylines(frame, [points], False, (230,230,0), 2)

            # Condition Pass the Line

            if limitsUp[0] < cx < limitsUp[2] and limitsUp[1] - 15 < cy < limitsUp[3]:
                if person_id not in person_id_collector:
                    counter_up += 1
                    person_id_collector.append(person_id)

                    
            if limitsDown[0] < cx < limitsDown[2] and limitsDown[1] < cy < limitsDown[3] + 15:
                if person_id not in person_id_collector:
                    counter_down += 1
                    person_id_collector.append(person_id)

    cv2.putText(frame, f"Count_Up : {counter_up}, Count_down : {counter_down}", (50,100), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 255), 4)


    out.write(frame)
    cv2.imshow("frame", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()