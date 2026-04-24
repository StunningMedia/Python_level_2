class Monster:
    def __init__(self, naam, levens, schade):
        self.naam = naam
        self.levens = levens
        self.schade = schade

    def val_aan(self, doel):
        doel.levens -= self.schade
        print(f"\nDe {self.naam} valt {doel.naam} aan!")

    def toon_info(self):
        print(f"\nMonster naam: {self.naam}")
        print(f"Levens: {self.levens}")
        print(f"Schade: {self.schade}")


creeper = Monster("Creeper", 20, 10)
skelet = Monster("Skelet", 15, 8)

creeper.toon_info()
skelet.toon_info()

skelet.val_aan(creeper)
print(f"\nDe {creeper.naam} heeft nu {creeper.levens} levens over.")

creeper.toon_info()
skelet.toon_info()