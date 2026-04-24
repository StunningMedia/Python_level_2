class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")