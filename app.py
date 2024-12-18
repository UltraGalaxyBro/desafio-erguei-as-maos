import pygame
import tkinter as tk
from lyrics import letra_musica
from tkinter import PhotoImage

letra = letra_musica()

pygame.mixer.init()

musica_tocando = True
ultimo_verso = None

pygame.mixer.music.load("musica.MP3")


def atualizar_letra():
    global ultimo_verso
    tempo_atual = pygame.mixer.music.get_pos() / 1000
    for trecho in letra:

        if (
            tempo_atual >= trecho["tempo"] / 1000
            and tempo_atual < (trecho["tempo"] + 2000) / 1000
        ):
            label_letra.config(text=trecho["texto"])
            if trecho["texto"] != ultimo_verso:
                print(trecho["texto"])
                ultimo_verso = trecho["texto"]

            break
    janela.after(100, atualizar_letra)


def tocar_pausar():
    global musica_tocando
    if musica_tocando:
        pygame.mixer.music.pause()
        botao_play_pause.config(text="PLAY", bg="blue")
    else:
        pygame.mixer.music.unpause()
        botao_play_pause.config(text="PAUSE", bg="gray")
    musica_tocando = not musica_tocando


janela = tk.Tk()
janela.title("ERGUEI AS MÃOS - Padre Marcelo Rossi")

janela.geometry("500x600")

janela.eval('tk::PlaceWindow %s center' % janela.winfo_toplevel())

titulo_musica = tk.Label(
    janela,
    text="ERGUEI AS MÃOS - Padre Marcelo Rossi",
    font=("Helvetica", 16, "bold"),
    fg="black",
)
titulo_musica.pack(pady=10)

imagem_capa = PhotoImage(file="padre-marcelo.png")
label_imagem_capa = tk.Label(janela, image=imagem_capa)
label_imagem_capa.pack(pady=10)

botao_play_pause = tk.Button(
    janela,
    text="PAUSE",
    command=tocar_pausar,
    bg="gray",
    fg="white",
    font=("Arial", 12, "bold"),
)
botao_play_pause.pack_forget()

label_letra = tk.Label(
    janela, text="", font=("Helvetica", 14), wraplength=400, justify="center"
)
label_letra.pack(pady=20)


def iniciar():
    pygame.mixer.music.play()
    atualizar_letra()
    botao_play_pause.pack(pady=30)
    botao_iniciar.pack_forget()

botao_iniciar = tk.Button(
    janela,
    text="INICIAR",
    command=iniciar,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
)
botao_iniciar.pack(pady=30)

janela.mainloop()
