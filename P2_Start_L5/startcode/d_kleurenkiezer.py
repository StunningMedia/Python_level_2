import tkinter
from email import message
from tkinter import colorchooser, messagebox

# kleur kiezen
# kleur = colorchooser.askcolor()[1]

# achtergrondkleur op iets zetten
# item.config(bg=kleur)


window = tkinter.Tk()
window.title("GUI les")
window.geometry("300x200")


def kies_kleur():
    messagebox.showinfo("kies een kleur","eerst voor de knop")
    kleur = colorchooser.askcolor()[1]
    color_button.config(bg=kleur)
    messagebox.showinfo("kies een kleur","en nu voor het scherm !!")
    kleur = colorchooser.askcolor()[1]
    window.config(bg=kleur)

# Knop aanmaken
color_button = tkinter.Button(window, text="Kies een kleur !!!", command=kies_kleur)
color_button.pack()

window.mainloop()