from tkinter import *
from tkinter import ttk
from random import randint

window = Tk()
window.title("Passwordyst")
window.geometry("400x300")
window["bg"] = "#333333"

def generatePassword():
    passwordLength = entry.get()
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"@#$%^&*'
    pass1 = ""
    for i in range(int(passwordLength)):
        pass1 += alph[randint(0, len(alph)-1)]
    label["text"] = pass1

entry = ttk.Entry(width="10")
entry.pack(anchor=N, padx=6, pady=6)

gen = ttk.Button(
    padding="0",
    width="10",
    text="Gen",
    command=generatePassword)
gen.pack(anchor=N, padx=6, pady=6)

label = ttk.Label(
    text="Your password will be here",
    foreground="#ffffff",
    background="#222222") # создаем кнопку из пакета tkinter
label.pack(expand="True")    # размещаем кнопку в окне


















window.mainloop()
