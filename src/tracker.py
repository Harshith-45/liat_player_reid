from deep_sort_realtime.deepsort_tracker import DeepSort

class PlayerTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def update_tracks(self, bbox_xywh, confidences, frame):
        return self.tracker.update_tracks(bbox_xywh, confidences, frame=frame)
