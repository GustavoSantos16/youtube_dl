from pytube import YouTube, Playlist
from pytube.cli import on_progress
import os

# VIDEO_URL = 'https://www.youtube.com/watch?v=D26bLJ9ut88'
# PLAYLIST_URL = 'https://www.youtube.com/watch?v=Ck3jX3wbyfY&list=PLmHzN0jU_yECKq_7W0DASIGejHHrMgKw0&ab_channel=CortesdoLutz%5BOFICIAL%5D'


while True:
    #Limpando console
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    #Escolher tipo de download
    answer = int(input("Deseja fazer download de um video ou playlist ? \n [1]Vídeo\n [2]Playlist\n Resposta:"))


    if answer == 1:
        url_video = input("Digite a url do vídeo: ")
        yt = YouTube(url_video, on_progress_callback=on_progress)
        yt.streams.get_highest_resolution().download()
        break
    elif answer == 2:
        url_playlist = input("Digite a url da playlist: ")
        playlist = Playlist(url_playlist)

        for video in playlist:
            yt = YouTube(video, on_progress_callback=on_progress)
            yt.streams.get_highest_resolution().download()
        break
 
print("Download complete")








