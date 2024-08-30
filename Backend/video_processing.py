import cv2
from yolo_interface import detect_objects

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    detections = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_detections = detect_objects(frame)
        detections.append(frame_detections)

    cap.release()
    return detections
