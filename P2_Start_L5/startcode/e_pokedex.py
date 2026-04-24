import tkinter
import requests

from P2_Start_L2.solutions.extra2_disney import naam

window = tkinter.Tk()
window.title("GUI les")
window.geometry("400x600")

def haal_pokemon_informatie_op():
    url = 'https://pokeapi.co/api/v2/pokemon/' + naam.get()
    response = requests.get(url)
    data = response.json()
    pokemon_height = data["height"] * 10
    pokemon_weight = data["weight"] / 10
    base_experience = data['base_experience']
    pokemon_abilities = []
    for ability in data['abilities']:
        ability_naam = ability['ability']['name']
        pokemon_abilities.append(ability_naam)

    # Genereer de tekst voor weergave
    info_tekst = f"Naam: {naam.get()}\nHoogte: {pokemon_height} cm\nGewicht: {pokemon_weight} kg\n Mogelijkheden: {pokemon_abilities}"

    pokemon_info_label.config(text=info_tekst)

# label maken
label = tkinter.Label(window, text="Welke pokemon wil je zoeken ?")
label.pack()
# een inputveld tonen
# tkinter.Entry(window)

naam = tkinter.Entry(window,width=50)
naam.pack()


pokemon_info_label = tkinter.Label(window, text="")
pokemon_info_label.pack()

haal_info_op_knop = tkinter.Button(window, text="Haal Pokémon Informatie op", command=haal_pokemon_informatie_op)
haal_info_op_knop.pack()

window.mainloop()

# url poke-api
# https://pokeapi.co/api/v2/pokemon/