import tkinter

window = tkinter.Tk()
window.title("GUI les")
window.geometry("300x200")

# label maken
label = tkinter.Label(window, text="Welkom bij mijn eerste GUI!")
label.pack()

# Functie om tekst van label aan te passen
def verander_tekst():
    label.config(text="Knop ingedrukt!")



# Functie om tekst van label aan te passen naar beginwaarde
def verander_tekst_terug():
    label.config(text="Welkom bij mijn eerste GUI!")

# Knop aanmaken
button = tkinter.Button(window, text="Klik op mij!", command=verander_tekst)
button.pack()


# reset Knop aanmaken
reset_button = tkinter.Button(window, text="Klik ook op mij!", command=verander_tekst_terug)
reset_button.pack()

# main loop van het scherù
window.mainloop()