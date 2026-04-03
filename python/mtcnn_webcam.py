import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

mtcnn = MTCNN(
    image_size=160,
    margin=20,
    min_face_size=40,
    thresholds=[0.6, 0.7, 0.7],
    factor=0.709,
    post_process=False,
    device=device
)

cap = cv2.VideoCapture(
    "/dev/v4l/by-id/usb-046d_C922_Pro_Stream_Webcam_5FBE37BF-video-index0",
    cv2.CAP_V4L2
)

# open the second webcam if the first one is not available
if not cap.isOpened():
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    raise RuntimeError("Cannot open webcam.")

# for faster processing, the resolution is set to 640x480.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_count = 0
boxes = None
probs = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read frame from webcam.")
        break

    # turn the frame from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # detect faces every 2 frames to improve performance, but still show the last detected boxes on every frame
    if frame_count % 2 == 0:
        boxes, probs = mtcnn.detect(rgb_frame)

    display = frame.copy()
    face_crop_to_show = None

    if boxes is not None:
        for box, prob in zip(boxes, probs):
            if box is None or prob is None:
                continue
            if prob < 0.90:
                continue

            # at this point, we have a reliable face detection, so we can draw the box and show the cropped face
            x1, y1, x2, y2 = box.astype(int)

            # keep the box within the frame boundaries
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(display.shape[1], x2)
            y2 = min(display.shape[0], y2)

            cv2.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                display,
                f"Face {prob:.2f}",
                (x1, max(20, y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            face_crop = frame[y1:y2, x1:x2]
            if face_crop.size > 0:
                face_crop_to_show = face_crop

            # for now, we only show the first detected face crop
            break

    cv2.imshow("Webcam - MTCNN Detection", display)

    if face_crop_to_show is not None:
        cv2.imshow("Face Crop", face_crop_to_show)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()