# download-video-youtube
Scritp Python para fazer download de vídeos do YouTube.

### Pré-requisitos

- [Python 3](https://www.python.org/downloads)

### Instalação

Instalação das dependências:

```bash
cd ~/.../download-video-youtube
pip install -r requirements.txt
```

### Executando o script

Preencha no arquivo **download.py** o link do vídeo do YouTube que deseja efetuar download conforme o exemplo.

```python
...
# preencher link do video
video_link = 'https://www.youtube.com/watch?v=3-kBGLAwRyY'
...
```

Execute o script utilizando o Python para realizar o download do vídeo.
```bash
cd ~/.../download-video-youtube
python download.py
```

Ao final da execução o arquivo gerado durante o processo de download estará disponível na pasta **downloads** do projeto.

```bash
cd ~/.../download-video-youtube/downloads
```