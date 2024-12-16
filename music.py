import pygame
import tkinter as tk

pygame.mixer.init()

musica_tocando = True

pygame.mixer.music.load("musica.MP3")
pygame.mixer.music.play()
   
def tocar_pausar():
    global musica_tocando
    if musica_tocando:
        pygame.mixer.music.pause()
        botao_play_pause.config(text="PLAY")
    else:
        pygame.mixer.music.unpause()
        botao_play_pause.config(text="PAUSE")
    musica_tocando = not musica_tocando

janela = tk.Tk()
janela.title("ERGUEI AS MÃOS - Padre Marcelo Rossi")

botao_play_pause = tk.Button(janela, text="PAUSE", command=tocar_pausar)
botao_play_pause.pack(pady=30)

janela.mainloop()
