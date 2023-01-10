import re
from pytube import YouTube
from pytube.cli import on_progress

r = re.compile(r'(?:\/watch\?v=|\/)([0-9A-Za-z_-]{11}).*')

# preencher link do video
video_link = 'link'

if r.search(video_link):

    # configurando a ferramenta
    yt = YouTube(video_link, on_progress_callback=on_progress)

    # detalhes do video
    print('Título: ', yt.title)
    print('Número de views: ', yt.views)
    print('Tamanho do vídeo: ', yt.length, 'segundos')
    print('Avaliação do vídeo: ', yt.rating)

    # seleciona a maior resolucao 
    ys = yt.streams.get_highest_resolution()

    # processar o download
    print('Iniciando download...')
    ys.download('./downloads')
    print('Download finalizado!')

else:

    print('video_link nao configurado')