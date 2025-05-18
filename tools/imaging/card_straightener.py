import cv2
import numpy as np
from PIL import Image

def straighten_and_crop(image_path, output_path, padding=20):

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # blur and detect edge
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    # find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        raise ValueError("No contours found.")

    # largest contour, card
    largest_contour = max(contours, key=cv2.contourArea)

    # approximate polygon of contour
    peri = cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, 0.02 * peri, True)
    if len(approx) != 4:
        raise ValueError("Detected contour is not quadrilateral.")

    # order points for perspective transform
    pts = approx.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # top-left
    rect[2] = pts[np.argmax(s)]  # bottom-right

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # top-right
    rect[3] = pts[np.argmax(diff)]  # bottom-left

    # compute new image size
    (tl, tr, br, bl) = rect
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxWidth = int(max(widthA, widthB))
    maxHeight = int(max(heightA, heightB))

    # destination rectangle with padding
    dst = np.array([
        [padding, padding],
        [maxWidth - 1 + padding, padding],
        [maxWidth - 1 + padding, maxHeight - 1 + padding],
        [padding, maxHeight - 1 + padding]
    ], dtype="float32")

    # adjust source points accordingly for transform
    src = rect

    # warp perspective
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth + 2*padding, maxHeight + 2*padding))

    # save
    result = Image.fromarray(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
    result.save(output_path)

    return output_path


if __name__ == "__main__":
    input_file = "ar01.jpg"
    output_file = "ar01_straightened.jpg"
    straighten_and_crop(input_file, output_file)