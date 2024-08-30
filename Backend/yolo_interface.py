import cv2
from ultralytics import YOLO

model = YOLO('models/yolov8n.pt')  

def detect_objects(image):
    results = model(image)    
    detections = []
    for result in results:
        for *xyxy, conf, cls in result.xyxy[0]: 
            label = model.names[int(cls)]
            detections.append({
                'label': label,
                'confidence': conf.item(),
                'bbox': [int(coord) for coord in xyxy]
            })
    return detections
