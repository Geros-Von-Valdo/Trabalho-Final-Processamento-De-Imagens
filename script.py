import cv2
import os
from ultralytics import YOLO
from tqdm import tqdm
import numpy as np
from skimage.metrics import structural_similarity as ssim
import logging

logging.getLogger('ultralytics').setLevel(logging.ERROR)

video_path = "video.mp4"
output_dir = "frames_sem_professors"
os.makedirs(output_dir, exist_ok=True)

model = YOLO('yolov5s.pt')

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

max_frames = int(min(total_frames, (3*60 + 50) * fps))

frames_salvos = 0
ultimo_frame_salvo = None

pbar = tqdm(total=max_frames, desc="Processando vídeo", unit="frame")

frame_idx = 0
while frame_idx < max_frames:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    tem_pessoa = False
    for result in results:
        for det in result.boxes.data.cpu().numpy():
            class_id = int(det[5])
            conf = det[4]
            if class_id == 0 and conf > 0.3:
                tem_pessoa = True
                break
        if tem_pessoa:
            break

    if not tem_pessoa:
        if ultimo_frame_salvo is not None:
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ultimo_gray = cv2.cvtColor(ultimo_frame_salvo, cv2.COLOR_BGR2GRAY)
            similarity = ssim(frame_gray, ultimo_gray)
            if similarity > 0.95:
                frame_idx += 1
                pbar.update(1)
                continue

        filename = os.path.join(output_dir, f"frame_{frame_idx:06d}.png")
        cv2.imwrite(filename, frame)
        ultimo_frame_salvo = frame.copy()
        frames_salvos += 1

    frame_idx += 1
    pbar.update(1)

pbar.close()
print(f"Finalizado! {frames_salvos} frames salvos na pasta '{output_dir}'.")
cap.release()
