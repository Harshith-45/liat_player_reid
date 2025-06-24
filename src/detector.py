from ultralytics import YOLO

class PlayerDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model.predict(source=frame, conf=0.3, save=False, imgsz=320, device='cpu')
        detections = []

        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]
                bbox = box.xyxy[0].tolist()
                detections.append((bbox, label))
                print(f"[DEBUG] Detected class: {label}")
        return detections
