from ultralytics import YOLO
import cv2

# Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")  # small version for speed

# Open webcam
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Draw results
    annotated_frame = results[0].plot()

    cv2.imshow("Traffic Light Detection Demo", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows() 

