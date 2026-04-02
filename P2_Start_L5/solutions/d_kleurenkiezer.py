import tkinter
from tkinter import colorchooser

#  hier de functie die wwe dadelijk gaan koppelen aan de knop
def open_kleurkiezer():
    # als deze functie wordt aangeroepen gaan we variabele "kleur" vullen met het resultaat van de kleurenkiezer
    kleur = colorchooser.askcolor()[1]
    #  en als er een geldige kleur gekozen is gebruiken we die als achtergrondkleur voor de knop
    if kleur:
        knop.config(bg=kleur)  # Je kan hier ook window gebruiken i.p.v. knop


# maak een scherm op de standaard manier
window = tkinter.Tk()
window.title("Kleurkiezer Oefening")
window.geometry("300x200")

# en maak een knop om de functie open_kleurkiezer aan te hangen
knop = tkinter.Button(window, text="Kies een kleur!", command=open_kleurkiezer)
knop.pack()


# start de main loop
window.mainloop()