import yt_dlp

# Link do vídeo que você quer baixar
video_url = "https://www.youtube.com/watch?v=JgGseIonmYI"  # Você pode trocar aqui

# Pasta de saída (opcional)
output_path = "videos/%(title)s.%(ext)s"

# Configurações de download
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': output_path,
    'merge_output_format': 'mp4',
    'quiet': False,
    'noplaylist': True,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }]
}

# Executa o download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print(f"Baixando vídeo de: {video_url}")
    ydl.download([video_url])
    print("Download finalizado.")


