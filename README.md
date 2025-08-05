# 🎥 Processamento Inteligente de Aulas em Vídeo com YOLO e Python

Este projeto tem como objetivo extrair automaticamente imagens significativas de uma vídeo-aula, **ignorando momentos em que o professor aparece no quadro**. O sistema utiliza **YOLOv5** para detecção de pessoas e técnicas de **visão computacional** para comparar quadros e evitar salvar imagens repetidas. As imagens extraídas são salvas para posterior consulta dos alunos.

---

## 🧠 Objetivo

Facilitar o registro visual do conteúdo escrito em quadro durante aulas presenciais gravadas, **preservando a privacidade do professor** e **otimizando o uso de imagens limpas**, onde o conteúdo está visível sem obstruções.

---

## ⚙️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [YOLOv5](https://github.com/ultralytics/yolov5) (via `ultralytics`)
- [NumPy](https://numpy.org/)
- [scikit-image](https://scikit-image.org/) – para cálculo de similaridade (SSIM)
- [tqdm](https://github.com/tqdm/tqdm) – barra de progresso

---

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
