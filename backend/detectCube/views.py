from django.shortcuts import render
from django.http import JsonResponse
import json
import cv2
import numpy as np
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings

import base64


def get_color_name(h, s, v):
    print(h, s, v)
    if s < 65 and v > 50:
        return "white"
    if 178 <= h or 0 <= h < 27:
        return "orange"
    if 27 <= h < 45:
        return "yellow"
    if 45 <= h < 85:
        return "green"
    if 85 <= h < 160:
        return "blue"
    if h <= 1 or h > 160:
        return "red"
    return "Unknown"


def get_dominant_rgb_color(roi):
    """Get dominant RGB from a certain region of interest.

    :param roi: the image array
    :returns: tuple
    """
    pixels = np.float32(roi.reshape(-1, 3))

    n_colors = 7
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant = palette[np.argmax(counts)]
    hsv_frame = cv2.cvtColor(np.uint8([[dominant]]), cv2.COLOR_BGR2HSV)[0][0]
    [h, s, v] = hsv_frame
    color = get_color_name(h, s, v)
    return color


@csrf_exempt
def scan_view(request):
    if request.method == "POST":
        save_dir = os.path.join(settings.BASE_DIR, "decoded_images")
        os.makedirs(save_dir, exist_ok=True)

        data = json.loads(request.body)
        face = data.get("face")
        colors = []
        for idx, image_data in enumerate(face):
            if "," in image_data:
                image_data = image_data.split(",")[1]

            missing_padding = len(image_data) % 4
            if missing_padding:
                image_data += "=" * (4 - missing_padding)

            img_decoded = base64.b64decode(image_data)
            img_array = np.frombuffer(img_decoded, np.uint8)
            image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            filename = f"decoded_image_{idx + 1}.jpg"
            save_path = os.path.join(save_dir, filename)
            cv2.imwrite(save_path, image)

            blurredFrame = cv2.blur(image, (3, 3))
            color = get_dominant_rgb_color(blurredFrame)
            colors.append(color)
        print(colors)
        return JsonResponse({"colors": colors})
