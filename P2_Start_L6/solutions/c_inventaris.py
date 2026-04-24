# definitie van de klasse "Inventaris"
class Inventaris:

    # de constructor doet niet veel, zet enkel een lege lijst klaar in property "wagens"
    def __init__(self):
        self.wagens = []

    # de functie "voeg_auto_toe" neemt een auto als parameter, en voegt die toe aan de lijst in "wagens"
    def voeg_auto_toe(self, auto):
        self.wagens.append(auto)

    #de functie "verwijder_auto" neemt een auto als parameter, en als die in de lijst "wagens" zit wordt die eruit gehaald
    def verwijder_auto(self, auto):
        if auto in self.wagens:
            self.wagens.remove(auto)
        else:
            print("Auto niet gevonden in inventaris")

    # de functie "toon_inventaris" loopt over alle auto's in "wagens" en drukt ze één voor één af
    def toon_inventaris(self):

        print("hier komt de lijst auto's")
        for auto in self.wagens:
            print(f"{auto.merk} {auto.model} ({auto.jaar})")
        print("")

# definitie van klasse "Auto"
class Auto:
    #  de constructor zet merk, model en jaar gereed
    def __init__(self, merk, model, jaar):
        self.merk = merk
        self.model = model
        self.jaar = jaar

# tot zover de klasse definities.   Alle code hierboven heeft alleen nog maar dingen gedefinieerd, er nog niks mee gedaan

# nu maken we een object van klasse "Inventaris" aan en houden het bij in variabele "inventaris"

inventaris = Inventaris()

#  dan maken we twee objecten aan van klasse "Auto"
auto1 = Auto("Volvo", "V40", 2018)
auto2 = Auto("Toyota", "Supra", 2006)

#  voeg de twee auto's toe aan de inventaris, en druk af
inventaris.voeg_auto_toe(auto1)
inventaris.voeg_auto_toe(auto2)
inventaris.toon_inventaris()

# verwijder de eerste auto terug, en druk nogmaals af
inventaris.verwijder_auto(auto1)
inventaris.toon_inventaris()