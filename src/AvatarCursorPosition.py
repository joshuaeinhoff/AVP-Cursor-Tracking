import os
import sys
import glob
import time
import cv2
import numpy as np
import json
from ultralytics import YOLO

model_path = '../model/model.pt'
video_source = '../data/video/742853_case1.mp4'
min_threshold = 0.65
filename = '742853_case1.json'
# parse video until and decrease threshold until only one cursor is found

model = YOLO(model_path, task='detect')
labels = model.names

cap = cv2.VideoCapture(video_source)
bbox_colors = [(164,120,87), (68,148,228)]

AvatarCenterHeadOffset = 35
avg_frame_rate = 0
frame_rate_buffer = []
fps_avg_len = 200
frame_count = 0
data = []
while True:
    t_start = time.perf_counter()

    ret, frame = cap.read()
    if not ret:
        print('Reached end of the video file. Exiting program.')
        break
    #frame = cv2.resize(frame, (1920, 1080))
    results = model(frame, verbose=False)
    detections = results[0].boxes
    object_count = 0
    for i in range(len(detections)):

        # Get bounding box coordinates
        # Ultralytics returns results in Tensor format, which have to be converted to a regular Python array
        xyxy_tensor = detections[i].xyxy.cpu()  # Detections in Tensor format in CPU memory
        xyxy = xyxy_tensor.numpy().squeeze()  # Convert tensors to Numpy array
        xmin, ymin, xmax, ymax = xyxy.astype(int)  # Extract individual coordinates and convert to int

        # Get bounding box class ID and name
        classidx = int(detections[i].cls.item())
        classname = labels[classidx]

        # Get bounding box confidence
        conf = detections[i].conf.item()

        # Draw box if confidence threshold is high enough
        if conf > 0.5:
            color = bbox_colors[classidx % 10]
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)

            #calculate center point
            xcenter = int((xmin+xmax)/2)
            ycenter = int((ymin+ymax)/2)
            cv2.circle(frame, (xcenter, ycenter), 4, color, -1)

            if classname == 'Avatar':
                yvalueHead = int(ymin+AvatarCenterHeadOffset)
                cv2.circle(frame,(xcenter,yvalueHead),4, color, -1)
                data.append(('Avatar',xcenter, yvalueHead, frame_count))
            else:
                data.append(('Cursor', xcenter, ycenter, frame_count))

            label = f'{classname}: {int(conf * 100)}%'
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)  # Get font size
            label_ymin = max(ymin, labelSize[1] + 10)  # Make sure not to draw label too close to top of window
            cv2.rectangle(frame, (xmin, label_ymin - labelSize[1] - 10),
                          (xmin + labelSize[0], label_ymin + baseLine - 10), color,
                          cv2.FILLED)  # Draw white box to put label text in
            cv2.putText(frame, label, (xmin, label_ymin - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0),
                        1)  # Draw label text
            # Basic example: count the number of objects in the image
            object_count = object_count + 1

    frame_count += 1
    #cv2.putText(frame, f'FPS: {avg_frame_rate:0.2f}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 255, 255), 2)  # Draw framerate
    cv2.putText(frame, f'Number of objects: {object_count}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 255, 255), 2)  # Draw total number of detected objects
    cv2.imshow('YOLO detection results', frame)  # Display image
    key = cv2.waitKey(5)
    if key == ord('q') or key == ord('Q'):  # Press 'q' to quit
        break
        # Calculate FPS for this frame
        t_stop = time.perf_counter()
        frame_rate_calc = float(1 / (t_stop - t_start))

print(data)
cap.release()
cv2.destroyAllWindows()

f = open(filename, 'x')
json.dump(data, f)