# een inputveld tonen
# tkinter.Entry(window)

# url poke-api
# https://pokeapi.co/api/v2/pokemon/

import tkinter
import requests
from PIL import Image, ImageTk
import io

# hier alvast de functie om echte pokemon gegevens van het internet te plukken
def haal_pokemon_informatie_op():
    # pak de ingevulde waarde van veld "pokemon_naam_entyr" en houd bij in variabele "pokemon_naam"  ( nog wel eerst omvormen naar alles kleine letters
    pokemon_naam = pokemon_naam_entry.get().lower() # Haal pokémonnaam op in kleine letters

    # bouw het adres om de pokemon gegevens op te halen
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_naam}"
    #  en voer dan het request uit.    Houd het resultaat bij in variabele "response"
    response = requests.get(api_url)

    #  als het gelukt is   ( status code = 200 ) ...
    if response.status_code == 200:
        # haal de json uit de response en houd bij in variabele "data"
        data = response.json()

        # Extract de benodigde informatie
        naam = data['name']
        hoogte = data['height'] * 10  # Hoogte is in decimetres, omzetten naar centimeters
        gewicht = data['weight'] / 10  # Gewicht is in hectograms, omzetten naar kilograms
        base_experience = data['base_experience']
        # Maak een lege lijst waar we abilities aan gaan toevoegen.
        abilities = []
        # loop over alle abilities die in de json zitten en voeg toe aan de lijst
        for ability in data['abilities']:
            ability_naam = ability['ability']['name']
            abilities.append(ability_naam)

        # Genereer de tekst voor weergave
        info_tekst = f"Naam: {naam}\nHoogte: {hoogte} cm\nGewicht: {gewicht} kg\n" + f"Basiservaring: {base_experience}\nMogelijkheden: {abilities}"

        pokemon_info_label.config(text=info_tekst) # Plaats de infotekst
    else:
        # Als de Pokémon niet gevonden is, geef een melding weer
        pokemon_info_label.config(text="Pokémon niet gevonden")

# Creëer het hoofdvenster
window = tkinter.Tk()
window.title("Pokémon Informatie Applicatie")


pokemon_naam_label = tkinter.Label(window, text="Voer een Pokémon-naam in:")
pokemon_naam_label.pack()

pokemon_naam_entry = tkinter.Entry(window)
pokemon_naam_entry.pack()

pokemon_info_label = tkinter.Label(window, text="")
pokemon_info_label.pack()

haal_info_op_knop = tkinter.Button(window, text="Haal Pokémon Informatie op", command=haal_pokemon_informatie_op)
haal_info_op_knop.pack()



window.mainloop()  # Start de GUI-loop