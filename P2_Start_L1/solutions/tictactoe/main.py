# Maak een functie tic_tac_toe(), die ons hele hoofdprogramma bevat

# importeer alles van mytictactoe
from mytictactoe import *


# definitie van de hoofdfunctie
def tic_tac_toe():
    # initialiseren variabelen
    bord = initialiseer_bord()
    huidige_speler = 'X'
    einde_spel = False
    winnaar = ''
    teller = 0

    # zolang het spel niet gedaan is ....
    while not einde_spel:
        # toon het speelbord op het scherm
        print_bord(bord)

        # vraag aan de speler nieuwe rij en kolom te kiezen voor volgende zet
        rij = int(input("Kies een rij (0, 1, 2): "))
        kolom = int(input("Kies een kolom (0, 1, 2): "))

        # voer de gekozen zet uit op het bord
        bord = zet(bord, rij, kolom, huidige_speler)

        # en verhoog de teller zodat we niet boven de 9 beurten kunnen gaan
        teller += 1

        # controleer of er een winnaar is
        einde_spel = controleer_winnaar(bord)
        if einde_spel:
            winnaar = huidige_speler
        #  als er nog geen winnaar is:  wisselen van speler
        else:
            if huidige_speler == 'X':
                huidige_speler = 'O'
            else:
                huidige_speler = 'X'

        #  als er negen zetten gedaan zijn stop het spel
        if teller == 9:
            einde_spel = True


    # na de hoofdlus nog één maal het bord afdrukken
    print_bord(bord)
    # en winnaar of gelijkspel bekendmaken
    if winnaar == '':
        print("Het spel eindigt in gelijkspel.")
    else:
        print(f"Speler {winnaar} heeft gewonnen!")


tic_tac_toe()
