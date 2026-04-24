import tkinter

window = tkinter.Tk()
window.title("GUI les")
window.geometry("300x200")

# Functie om tekst van label aan te passen
def verander_tekst():
    label.config(text="Knop ingedrukt!")


# Functie om tekst van label aan te passen
def reset_tekst():
    label.config(text="Welkom bij mijn eerste gui, de reset versie !")


# label maken
label = tkinter.Label(window, text="Welkom bij mijn eerste GUI!")
label.pack()



# Knop aanmaken
button = tkinter.Button(window, text="Klik op mij!", command=verander_tekst)
button.pack()



# Knop aanmaken
reset_button = tkinter.Button(window, text="reset de tekst", command=reset_tekst)
reset_button.pack()


window.mainloop()

