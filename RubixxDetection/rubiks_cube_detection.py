import cv2
import numpy as np

# Function to get the color name based on HSV values
def get_color_name(h, s, v):
    if s < 10 and v > 200:
        return "White"
    if v < 50:
        return "Black"
    if h < 10 or h > 160:
        return "Red"
    if 10 <= h < 25:
        return "Orange"
    if 25 <= h < 35:
        return "Yellow"
    if 35 <= h < 85:
        return "Green"
    if 85 <= h < 125:
        return "Blue"
    if 125 <= h < 160:
        return "Purple"
    return "Unknown"

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges for the Rubik's Cube
    color_ranges = {
        "red": [(0, 100, 100), (10, 255, 255), (160, 100, 100), (180, 255, 255)],
        "green": [(40, 100, 100), (80, 255, 255)],
        "blue": [(100, 100, 100), (140, 255, 255)],
        "yellow": [(20, 100, 100), (30, 255, 255)],
        "white": [(0, 0, 200), (180, 25, 255)],
        "orange": [(10, 100, 100), (25, 255, 255)]
    }

    for color, ranges in color_ranges.items():
        if len(ranges) == 2:
            lower, upper = ranges
            mask = cv2.inRange(hsv_frame, np.array(lower), np.array(upper))
        else:
            mask1 = cv2.inRange(hsv_frame, np.array(ranges[0]), np.array(ranges[1]))
            mask2 = cv2.inRange(hsv_frame, np.array(ranges[2]), np.array(ranges[3]))
            mask = mask1 | mask2

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)

            # Filter by area (ignore too small or too large objects)
            if 500 < area < 5000:
                # Approximate the contour to get more accurate shape
                perimeter = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

                # Filter based on the number of approximated corners (square detection)
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)

                    # Aspect ratio filtering (cube's face is roughly square)
                    aspect_ratio = w / float(h)
                    if 0.9 <= aspect_ratio <= 1.1:  # Close to square shape
                        # Get the region of interest (the square area)
                        roi = hsv_frame[y:y+h, x:x+w]

                        # Calculate the average HSV color in the square
                        avg_h = np.mean(roi[:, :, 0])
                        avg_s = np.mean(roi[:, :, 1])
                        avg_v = np.mean(roi[:, :, 2])

                        # Get the color name based on the average HSV values
                        color_name = get_color_name(avg_h, avg_s, avg_v)

                        # Draw a bounding box around the detected square
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        # Display the color name on the square
                        cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Show the frame with detected squares and labeled colors
    cv2.imshow('Square Detection and Color Labeling', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
