# definitie van de klasse "pizza"
class Pizza:
    # constructor slaat naam en grootte op in interne variabelen
    def __init__(self, naam, grootte):
        self.naam = naam
        self.grootte = grootte

    # de functie toon_informatie beeldt de info van de pizza af op het scherm
    def toon_informatie(self):
        print(f"\nNaam: {self.naam}")
        print(f"Grootte: {self.grootte}")

# nu maken we drie verschillende pizza's
pizza1 = Pizza("Margherita", "medium")
pizza2 = Pizza("Pepperoni", "groot")
pizza3 = Pizza("Hawaï", "klein")

# en we laten ze één voor één hun informatie tonen
pizza1.toon_informatie()
pizza2.toon_informatie()
pizza3.toon_informatie()