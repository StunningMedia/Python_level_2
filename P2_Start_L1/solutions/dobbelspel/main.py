from dobbelspel import dobbel


def speel_dobbelspel():
    print("Welkom in het dobbel spel!")
    speel_opnieuw = "ja"
    while speel_opnieuw.lower() == "ja":
        dobbel()
        speel_opnieuw = input("Wil je opnieuw spelen? (ja/nee): ")

    print("bedankt om te spelen!")

speel_dobbelspel()