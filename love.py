import tkinter as tk
from tkinter import  PhotoImage, Canvas, Button, END
import pandas as pd
import os
import random


root = tk.Tk()
root.title("MENU")
root.geometry("500x500")
root.grab_set()
root.focus_force()

def fechar():
    try:
        root.destroy()
    except Exception as erro:
        print(erro)
        pass



def spamlove():
    
    msg_love = [
    "Eu te amo mais do que as palavras podem expressar.",
    "Você é a pessoa que ilumina a minha vida.",
    "Meu amor por você é infinito e eterno.",
    "Você é o meu porto seguro, meu amor.",
    "Ao seu lado, eu sou a pessoa mais feliz do mundo.",
    "Não consigo imaginar minha vida sem você, meu amor.",
    "O seu sorriso é a coisa mais bonita que já vi.",
    "Seu abraço é o meu lugar favorito no mundo.",
    "Você é o meu sonho realizado, meu amor.",
    "Meu coração bate mais forte por você, eu te amo."]
    
    for m in msg_love:
        # Cria uma nova janela
        window = tk.Toplevel(root)
        window.title("Janela do Amor")
        
        # Define a posição aleatória da janela na tela
        x = random.randint(0, root.winfo_screenwidth() - 200)
        y = random.randint(0, root.winfo_screenheight() - 200)
        window.geometry(f"500x50+{x}+{y}")
        
        # Escolhe uma mensagem aleatória de amor

        
        # Cria um rótulo na janela com a mensagem
        label = tk.Label(window, text=m, font=("Arial", 12))
        label.pack(pady=10)

root.resizable(width=False, height=False)

bg = PhotoImage(file=r'bk_img.png')
tela = Canvas(root, width=400, height=400)
tela.pack(fill="both", expand=True)
tela.create_image(0, 0, image=bg, anchor="nw")


image = tk.PhotoImage(file=r"heart.png", format="png")
heart = image.subsample(10, 10)
button_heart = Button(image=heart, relief="flat", command=spamlove)
button_heart.place(x=220, y=150)
button_heart.bind('<Enter>', lambda e: button_heart.config(bg='pink', fg='white'))
button_heart.bind('<Leave>', lambda e: button_heart.config(bg='white', fg="white"))

label_button = tk.Label(root, text=f"CLIQUE NO CORAÇÃO.", width=3, font=("Montserrat", 9), bg="pink", fg="black")
label_button.place(width=320, height=25, x=100, y=100)


root.protocol("WM_DELETE_WINDOW",fechar)
root.mainloop()
