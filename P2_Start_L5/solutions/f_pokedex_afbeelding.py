# een inputveld tonen
# tkinter.Entry(window)

# url poke-api
# https://pokeapi.co/api/v2/pokemon/

import tkinter
import requests
from PIL import Image, ImageTk
import io

#  nu komt er een functie bij waarmee we de afbeelding kunnen laden
def laad_afbeelding(image_url):
    # we halen op wat er te vinden is op het adres dat binnenkomt als parameter "image_url"
    response = requests.get(image_url)
    #  als het goed gegaan is   ( code = 200, dwz er is een geldige image gevonden )
    if response.status_code == 200:
        #  dan halen we de afbeelding uit de content van de response, en openen die afbeelding als een bit-stream
        afbeelding_data = response.content
        afbeelding = Image.open(io.BytesIO(afbeelding_data))
        photo = ImageTk.PhotoImage(afbeelding)
        image_label.config(image=photo)
        image_label.image = photo

def haal_pokemon_informatie_op():
    pokemon_naam = pokemon_naam_entry.get().lower() # Haal pokémonnaam op in kleine letters

    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_naam}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        # Extract de benodigde informatie
        naam = data['name']
        hoogte = data['height'] * 10  # Hoogte is in decimetres, omzetten naar centimeters
        gewicht = data['weight'] / 10  # Gewicht is in hectograms, omzetten naar kilograms
        base_experience = data['base_experience']
        # Maak een lege lijst waar we abilities aan gaan toevoegen.
        abilities = []
        for ability in data['abilities']:
            ability_naam = ability['ability']['name']
            abilities.append(ability_naam)

        # Genereer de tekst voor weergave
        info_tekst = f"Naam: {naam}\nHoogte: {hoogte} cm\nGewicht: {gewicht} kg\n" + f"Basiservaring: {base_experience}\nMogelijkheden: {abilities}"

        pokemon_info_label.config(text=info_tekst) # Plaats de infotekst

        image_url = data['sprites']['front_default']
        laad_afbeelding(image_url)
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

image_label = tkinter.Label(window)
image_label.pack()


window.mainloop()  # Start de GUI-loop