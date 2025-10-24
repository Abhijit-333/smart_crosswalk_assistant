import cv2
import numpy as np

def detect_crosswalk(image_path):
    # Load image
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Image not found.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Detect lines using Hough transform
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100,
                            minLineLength=100, maxLineGap=10)

    # Draw lines
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow("Crosswalk Line Detection", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    detect_crosswalk("data/test_crosswalk.jpeg")
