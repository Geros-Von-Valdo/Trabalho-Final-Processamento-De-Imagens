import cv2
import sys

# === CONFIGURAÇÃO ===
nome_imagem = "00-08.png"     # Altere aqui com o nome da imagem
nome_video = "00-08.mp4"     # Nome do arquivo de saída
duracao_segundos = 7
fps = 30                           # Frames por segundo

# === CARREGAR IMAGEM ===
img = cv2.imread(nome_imagem)
if img is None:
    print(f"Erro: não foi possível carregar '{nome_imagem}'")
    sys.exit(1)

altura, largura, _ = img.shape
total_frames = fps * duracao_segundos

# === CRIAR VÍDEO ===
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(nome_video, fourcc, fps, (largura, altura))

for _ in range(total_frames):
    video.write(img)

video.release()
print(f"Vídeo de 7 segundos criado como '{nome_video}' com sucesso.")
