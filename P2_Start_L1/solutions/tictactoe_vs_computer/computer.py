# importeer alles van mytictactoe
from mytictactoe import *
# we gaan ook random gebruiken
import random

# functie computer_zet:  gaat de beste zet voor de computer bepalen
#  strategie:
#       1. als de computer met een zet kan winnen, doet hij die
#       2. als hij niet direct kan winnen, gaat hij controleren of de tegenspeler in een volgende zet kan winnen.
#       als dat zo is, zal de computer op dat vakje een zet doen om tegenspeler te blokkeren
#       3. als hij niet direct kan winnen en niets moet blokkeren, doet hij een random zet
def computer_zet(bord, speler, tegenspeler):
    # kijk voor overwinning in de huidige beurt
    rij, kolom = vind_beste_zet(bord, speler)

    if not rij:  # Geen beste zet gevonden
        # kijk of de tegenspeler kan winnen in de volgende beurt
        rij, kolom = vind_beste_zet(bord, tegenspeler)

        if not rij:  # Weer geen beste zet gevonden
            rij, kolom = random_zet(bord)

    return rij, kolom

# functie random_zet:  om de computer een willekeurig leeg vak te laten kiezen
def random_zet(bord):
    # herhaal oneindig lang  ( tot je een vak gevonden hebt )
    while True:
        # zet rij en kolom op random waarden tussen 0 en 2
        rij = random.randint(0, 2)
        kolom = random.randint(0, 2)

        #  als op die plaats  ( rij, kolom ) nog geen symbool staat
        if bord[rij][kolom] == ' ':
            bord[rij][kolom] = ' '
            #  ...  geef dan die rij en kolom terug als resultaat van de functie
            return rij, kolom

# functie vind_beste_zet:  hiermee willen we nagaan of de speler met één zet kan winnen
def vind_beste_zet(bord, speler):
    # ga over alle rijen
    for rij in range(3):
        # ga in de rij over alle vakjes
        for kolom in range(3):
            # als het vakje dat je vindt leeg is
            if bord[rij][kolom] == ' ':
                # zet er dan het symbool van de speler in om te testen of je zo kan winnen
                bord[rij][kolom] = speler

                # roep dan de functie controleer_winnaar aan die we al hadden in mytictactoe
                # als die fuctie true geeft, betekent dit dat door deze zet te doen de speler zal winnen
                if controleer_winnaar(bord):  # Als er een winnaar is (True)
                    # zet dan het vakje terug leeg
                    bord[rij][kolom] = ' '
                    # en geef de rij en kolom terug als resultaat van de functie
                    return rij, kolom
                # ook als je er niet mee kan winnen, het vakje terug leeg maken
                bord[rij][kolom] = ' '
    # als je over alle rijen en vakjes bent gegaan en geen winnend vak gevonden hebt,
    #  dan zetten we rij en kolom weer leeg en geven die terug als resultaat van de functie
    rij = None
    kolom = None
    return rij, kolom



