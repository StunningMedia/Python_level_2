# definitie van de klasse "pizza"
class Pizza:
    # constructor slaat naam en grootte op in interne variabelen, en ook een lijst "toppings"
    def __init__(self, naam, grootte, toppings):
        self.naam = naam
        self.grootte = grootte
        self.toppings = toppings
        # we gaan nu ook de prijs berekenen en bijhouden
        self.prijs = self.bereken_prijs()

    # de functie toon_informatie beeldt de info van de pizza af op het scherm
    def toon_informatie(self):
        print(f"\nNaam: {self.naam}")
        print(f"Grootte: {self.grootte}")
        # om de toppings te tonen slaan we de lijst plat naar comma-separated
        print("Toppings:", ", ".join(self.toppings))
        print(f"Prijs: €{self.prijs:.2f}")

    # met deze functie kunnen we de prijs berekenen
    def bereken_prijs(self):
        basisprijs = 0.00
        if self.grootte == "klein":
            basisprijs = 8.99
        elif self.grootte == "medium":
            basisprijs = 10.99
        elif self.grootte == "groot":
            basisprijs = 12.99

        topping_prijs = len(self.toppings) * 1.50

        return basisprijs + topping_prijs



# nu maken we drie verschillende pizza's, met elk hun eigen grootte en toppingsq
pizza1 = Pizza("Margherita", "medium", ["kaas", "tomatensaus"])
pizza2 = Pizza("Pepperoni", "groot", ["kaas", "tomatensaus", "pepperoni"])
pizza3 = Pizza("Hawaï", "klein", ["kaas", "tomatensaus", "ham", "ananas"])

# en we laten ze één voor één hun informatie tonen
pizza1.toon_informatie()
pizza2.toon_informatie()
pizza3.toon_informatie()