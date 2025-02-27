import tkinter as tk
import pygame
import os
from PIL import Image, ImageTk

def notifica(txt, icon=None, sound=None, fg_rexcolor=None, toplevel=False, tempo=4000, callback=None):
    """Exibe uma notificação com suporte a som, ícone e callback ao clique."""
    
    # Garantir que tempo esteja no intervalo permitido
    tempo = max(500, min(tempo, 4000))

    def play_sound(sound_file):
        """Toca o som se o arquivo existir."""
        if sound_file and os.path.exists(sound_file):
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
            except Exception as e:
                print(f"Erro ao tocar som: {e}")

    def on_click(event):
        """Determina a ação ao clicar na notificação."""
        if event.x <= 30:  # Se o clique for nos primeiros 30px, fecha a notificação
            root.destroy()
        elif callback:  # Se houver um callback, chama a função
            callback()

    root = tk.Toplevel() if toplevel else tk.Tk()
    root.title("Sistema de notificações TK por Valdemir")
    root.wm_attributes("-topmost", 1)
    root.overrideredirect(True)
    root.configure(bg=fg_rexcolor if fg_rexcolor else "#2E2E2E")

    frame = tk.Frame(root, bg=root["bg"])
    frame.pack(padx=10, pady=10)

    # Carregar imagem, se disponível
    if icon and os.path.exists(icon):
        try:
            image = Image.open(icon)
            imagem_tk = ImageTk.PhotoImage(image)
            label = tk.Label(frame, image=imagem_tk, bg=root["bg"])
            label.image = imagem_tk  # Evita que o garbage collector remova a imagem
            label.pack(side="left", padx=5, pady=5)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

    # Texto da notificação
    lbl = tk.Label(frame, font=('calibri', 20, 'bold'), text=txt, bg=root["bg"], fg="white")
    lbl.pack(side="right", padx=5, pady=5, fill="both", expand=True)

    # Mapeamento de sons predefinidos
    sound_map = {
        "avaste": "notify/mp3/notf.mp3",
        "eroza": "notify/mp3/Erro.mp3",
        "atento": "notify/mp3/Atencao.mp3",
        "info": "notify/mp3/info.mp3"
    }
    sound_file = sound_map.get(sound, sound)  # Usa o arquivo fornecido se não for um dos predefinidos
    play_sound(sound_file)

    # Configurar clique na janela
    root.bind("<Button-1>", on_click)

    # Fecha após o tempo definido
    root.after(tempo, lambda: root.destroy())

    root.mainloop()
