import cv2
import random
from cvzone.FaceDetectionModule import FaceDetector

# Open webcam (use 0 for default camera or replace with image path)
cap = cv2.VideoCapture(0)

# Initialize detector
detector = FaceDetector(minDetectionCon=0.5)

# Ghost boxes state (two squares)
ghosts = [
    {"x": None, "y": None, "size": 120, "label": " 92%"},
    {"x": None, "y": None, "size": 120, "label": " 90%"},
]
frame_count = 0

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect face (cvzone detection only; drawing disabled)
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        for bbox in bboxs:
            x, y, w, h = bbox["bbox"]

            # Example fixed attributes (you can replace with AI model later)
            age = "21-25"
            mood = "Scared"
            gender = "Male"

            # Draw green rectangle around the face (no confidence)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Draw filled green box below for info
            # cv2.rectangle(img, (x, y + h), (x + w, y + h + 70), (0, 255, 0), cv2.FILLED)

            # Add text
            cv2.putText(img, f"Age: {age}", (x, y + h + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
            cv2.putText(img, f"Mood: {mood}", (x, y + h + 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
            cv2.putText(img, f"Gender: {gender}", (x, y + h + 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    
    # --- Fake "ghost detector" boxes at random places ---
    frame_count += 1
    h_img, w_img = img.shape[:2]
    for g in ghosts:
        size = g["size"]
        # Reposition occasionally
        if g["x"] is None or g["y"] is None or frame_count % 45 == 0:
            g["x"] = random.randint(10, max(10, w_img - size - 10))
            g["y"] = random.randint(10, max(10, h_img - size - 10))

        gx, gy = g["x"], g["y"]

        # Main detection square box
        cv2.rectangle(img, (gx, gy), (gx + size, gy + size), (0, 255, 0), 2)

        # Top label (confidence)
        label_text = g["label"]
        (tw, th), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        label_h = th + 10
        label_w = tw + 12
        label_x1 = gx
        label_y1 = max(0, gy - label_h)
        label_x2 = label_x1 + label_w
        label_y2 = label_y1 + label_h
        # cv2.rectangle(img, (label_x1, label_y1), (label_x2, label_y2), (0, 255, 0), cv2.FILLED)
        # cv2.putText(img, label_text, (label_x1 + 6, label_y2 - 6),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Info box under detection box
        info_lines = ["Age: 200-250", "Mood: Angry", "Gender: Unknown"]
        info_line_height = 22
        info_pad = 8
        info_height = info_pad * 2 + info_line_height * len(info_lines)
        info_y1 = gy + size + 6
        # Keep on screen vertically
        if info_y1 + info_height > h_img - 5:
            info_y1 = max(5, gy - 6 - info_height)
        info_x1 = gx
        info_x2 = min(w_img - 5, info_x1 + max(size, 220))
        # cv2.rectangle(img, (info_x1, info_y1), (info_x2, info_y1 + info_height), (0, 0, 255), cv2.FILLED)
        for i, txt in enumerate(info_lines):
            ty = info_y1 + info_pad + (i + 1) * info_line_height - 4
            cv2.putText(img, txt, (info_x1 + 8, ty), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Face Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
