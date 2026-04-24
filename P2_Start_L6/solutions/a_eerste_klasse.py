#  de klasse definitie hebben we hier cadeau gekregen


class Dier:
    #  in de constructor worden de naam en het geluid die we meegeven als parameters opgeslagen in interne variabelen van het object 'self'
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    # de klasse dier heeft ook een functie "maak_geluid", die een tekst afdrukt
    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")


# de opdracht is nu om een hond, kat en koe object te maken

diesel = Dier("hond", "woef")
blinkie = Dier("kat","miauw")
bella = Dier("koe","boe")

#  en ze dan één voor één hun geluid te laten maken
diesel.maak_geluid()
blinkie.maak_geluid()
bella.maak_geluid()
