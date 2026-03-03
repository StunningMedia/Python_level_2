# Schrijf een functie is_getal_geraden die op basis van een gok en een geheim_nummer controleert of de gok correct was.
# Print hier een boodschap, en return de juiste waarde.

# gebruik de random library
import random

# functie is_getal_geraden:  parameters:  gok en geheim_getal
def is_getal_geraden(gok, geheim_nummer):
#    als gok gelijk is aan geheim_getal:  print "correct" en return True
    if gok == geheim_nummer:
        print("Correct!")
        return True
#        anders:  print "fout" en return False
    else:
        print("Fout, Probeer opnieuw!")
        return False

#  functie raad_het_getal:   parameter:  bovengrens
def raad_het_getal(bovengrens):
#     kies een willekeurig getal tussen 1 en bovengrens, houd bij in geheim_nummer
    geheim_nummer = random.randint(1, bovengrens)
    geraden = False

#     zolang het niet geraden is ...
    while not geraden:
#          ...  vraag een gok
        gok = int(input(f"Raad een getal (1-{bovengrens}): "))
#          ...  voer is_getal_geraden uit met parameters gok en geheim_nummer.  Houd resultaat van aanroep bij in geraden
        geraden = is_getal_geraden(gok, geheim_nummer)


#  aanroep hoofdfunctie
raad_het_getal(10)
# Schrijf een functie raad_het_getal, die op basis van een bovengrens het raadspel zal spelen.
