# definitie van de klasse "pizza"
class Pizza:
    # constructor slaat naam en grootte op in interne variabelen, en ook een lijst "toppings"
    def __init__(self, naam, grootte, toppings):
        self.naam = naam
        self.grootte = grootte
        self.toppings = toppings

    # de functie toon_informatie beeldt de info van de pizza af op het scherm
    def toon_informatie(self):
        print(f"\nNaam: {self.naam}")
        print(f"Grootte: {self.grootte}")
        # om de toppings te tonen slaan we de lijst plat naar comma-separated
        print("Toppings:", ", ".join(self.toppings))

# nu maken we drie verschillende pizza's, met elk hun eigen grootte en toppings
pizza1 = Pizza("Margherita", "medium", ["kaas", "tomatensaus"])
pizza2 = Pizza("Pepperoni", "groot", ["kaas", "tomatensaus", "pepperoni"])
pizza3 = Pizza("Hawaï", "klein", ["kaas", "tomatensaus", "ham", "ananas"])

# en we laten ze één voor één hun informatie tonen
pizza1.toon_informatie()
pizza2.toon_informatie()
pizza3.toon_informatie()