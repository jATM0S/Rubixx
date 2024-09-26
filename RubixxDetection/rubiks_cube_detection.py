from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    image_data = data['image']
    
    # Decode the base64 image
    img_data = base64.b64decode(image_data)
    img_array = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color_ranges = {
        "red": [(0, 100, 100), (10, 255, 255), (160, 100, 100), (180, 255, 255)],
        "green": [(40, 100, 100), (80, 255, 255)],
        "blue": [(100, 100, 100), (140, 255, 255)],
        "yellow": [(20, 100, 100), (30, 255, 255)],
        "white": [(0, 0, 200), (180, 25, 255)],
        "orange": [(10, 100, 100), (25, 255, 255)]
    }

    results = []

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
            if 500 < area < 5000:
                perimeter = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)
                    aspect_ratio = w / float(h)
                    if 0.9 <= aspect_ratio <= 1.1:
                        roi = hsv_frame[y:y+h, x:x+w]
                        avg_h = np.mean(roi[:, :, 0])
                        avg_s = np.mean(roi[:, :, 1])
                        avg_v = np.mean(roi[:, :, 2])
                        color_name = get_color_name(avg_h, avg_s, avg_v)

                        results.append({
                            "color": color_name,
                            "position": (x, y, w, h)
                        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
