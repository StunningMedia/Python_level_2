# functie initialiseer_bord.   Geen parameters.    Zet een leeg bord klaar
def initialiseer_bord():
    #   begin met een lege array in variabele "bord"
    bord = []
    #   drie rijen  ==> doe drie keer ...
    for rij in range(3):
        # begin met een lege array in variabele "rij_inhoud"
        rij_inhoud = []
        #  drie vakjes in elke rij ==> doe drie keer ...
        for kolom in range(3):
            # voeg spatie toe aan array "rij_inhoud"    ( append )
            rij_inhoud.append(' ')
        #  voeg "rij_inhoud" toe aan "bord"
        bord.append(rij_inhoud)
    # geef variabele bord terug als resultaat van de functie
    return bord

#  functie "zet".   Parameters:  bord, rij, kolom, speler
#   gaat in het gegeven bord, op de gegeven rij en kolom, het symbool van de gegeven speler zetten
def zet(bord, rij, kolom, speler):
    bord[rij][kolom] = speler   # "speler" is gelijk aan "X" of "O"
    return bord

# functie print_bord  :  parameter:  te printen bord
def print_bord(bord):
    # Print een lege lijn
    print()
    # ga over alle rijen
    for rij in bord:
        # print de rij-array, gescheiden door pipelines
        print('|'.join(rij))
        # print een horizontale streep  ( 5 min-tekens )
        print('-' * 5)

#  functie controleer_winnaar:  hiermee kunnen we checken of iemand gewonnen heeft
def controleer_winnaar(bord):
    #  als er horizontaal drie dezelfde staan, of vertikaal, of diagonaal ....
    if (controleer_horizontaal(bord)
        or controleer_verticaal(bord)
        or controleer_diagonaal(bord) ):
        #  ...  dan hebben we een winnaar  en geven we True terug als resultaat van de functie
        return True
    # ...  als er geen winnende richting is, dan geven we False terug
    return False

# functie controleer_horizontaal:  hiermee checken we of één van de rijen een winnende combo heeft
def controleer_horizontaal(bord):
# ga over alle rijen van het bord.   Voor elke rij controleren ...
    for rij in bord:
    #  als de drie cellen in de rij gelijk zijn  ( en niet leeg )  ...
        if rij[0] == rij[1] == rij[2] != ' ':
            # ...  dan hebben we een winnaar.  We springen dan direct uit de lus met return True
            return True
    # als we alle rijen bekeken hebben en nog steeds geen winnende combo gevonden hebben, dan geven we False terug
    return False


# functie controleer_verticaal:  hiermee checken we of één van de kolommen een winnende combo heeft
def controleer_verticaal(bord):
    # ga over alle kolom-posities die in de verschillende rijen aanwezig zijn   ( dus van 0 tot en met 2 )
    for kolom in range(3):
        #  als voor één van die kolomposities alle rijen op die positie hetzelfde hebben  ( en niet leeg ) ....
        if bord[0][kolom] == bord[1][kolom] == bord[2][kolom] != ' ':
            # ...  dan hebben we een winnaar.  We springen dan direct uit de lus met return True
            return True
    # als we alle kolommen bekeken hebben en nog steeds geen winnende combo gevonden hebben, dan geven we False terug
    return False


# functie controleer_diagonaal:  hiermee checken we of één van de diagonalen een winnende combo heeft
def controleer_diagonaal(bord):
    # als de cellen van linksboven naar rechtsonder hetzelfde zijn en niet leeg
    if bord[0][0] == bord[1][1] == bord[2][2] != ' ':
        # dan hebben we een winnaar
        return True
    # als de cellen van rechtsboven naar linksonder hetzelfde zijn en niet leeg
    if bord[0][2] == bord[1][1] == bord[2][0] != ' ':
        # dan hebben we een winnaar
        return True
    # als we beide diagonalen bekeken hebben en nog steeds geen winnende combo gevonden hebben, dan geven we False terug
    return False