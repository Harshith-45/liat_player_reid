# File: src/main.py

import cv2
import torch
from detector import PlayerDetector
from tracker import PlayerTracker

# Constants
VIDEO_PATH = "videos/broadcast.mp4"
MODEL_PATH = "models/player_detection.pt"
FRAME_SKIP = 5  # Skip every 5 frames to speed up processing
RESIZE_DIM = (640, 384)  # Resize resolution

# Initialize detector and tracker
detector = PlayerDetector(MODEL_PATH)
tracker = PlayerTracker()

print(f"[INFO] Processing {VIDEO_PATH}...")

cap = cv2.VideoCapture(VIDEO_PATH)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % FRAME_SKIP != 0:
        continue

    frame = cv2.resize(frame, RESIZE_DIM)

    detections = detector.detect(frame)

    bbox_xywh = []
    confidences = []

    for det in detections:
      if len(det) == 3:
          cls, xyxy, conf = det
      elif len(det) == 2:
          cls, xyxy = det
          conf = 1.0
      else:
          continue

      if cls == 'player':
          [x1, y1, x2, y2] = xyxy
          w = x2 - x1
          h = y2 - y1
          x = x1 + w / 2
          y = y1 + h / 2
          bbox_xywh.append([x, y, w, h])
          confidences.append(conf)


    tracks = tracker.update_tracks(bbox_xywh, confidences, frame)

    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, w, h = track.to_ltrb()
        cv2.rectangle(frame, (int(l), int(t)), (int(w), int(h)), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}", (int(l), int(t) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Player Re-ID", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()