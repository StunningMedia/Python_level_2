#definitie van klasse "Monster"
class Monster:
    # de constructor zet eigenschappenn naam, levens en schade
    def __init__(self, naam, levens, schade):
        self.naam = naam
        self.levens = levens
        self.schade = schade

    # de functie val_aan neemt als parameter genaamd "doel" een ander object van klasse Monster
    def val_aan(self, doel):
        #  verminder de levens van het doel met je eigen waarde voor schade
        doel.levens -= self.schade
        print(f"\nDe {self.naam} valt {doel.naam} aan!")

    # de functie "toon_info" zet alle eigenschappen van dit Monster op het scherm
    def toon_info(self):
        print(f"\nMonster naam: {self.naam}")
        print(f"Levens: {self.levens}")
        print(f"Schade: {self.schade}")


# tot zover de klasse definities.   Alle code hierboven heeft alleen nog maar dingen gedefinieerd, er nog niks mee gedaan

# nu maken we twee objecten  van klasse "Monster" aan, en noemen die creeper en skelet
creeper = Monster("Creeper", 20, 10)
skelet = Monster("Skelet", 15, 8)

# we tonen de info van beide monsters
creeper.toon_info()
skelet.toon_info()

# dan laten we het skelet de creeper aanvallen
skelet.val_aan(creeper)
print(f"\nDe {creeper.naam} heeft nu {creeper.levens} levens over.")

# en tenslotte zetten we nog eens de info van beide op het scherm
creeper.toon_info()
skelet.toon_info()