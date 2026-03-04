# Bekijk de documentatie voor de Disney API: https://disneyapi.dev/docs/
# Vraag aan de API alle personages.
#
# Print alle personages als volgt:
# Naam: Abu - Oorspronkelijke film: Aladdin (film)
# Naam: Abuelita - Oorspronkelijke film: Onbekend





# Zorg er voor dat je alle personages kan tonen.

import requests
# adres als je een beperkte set karakters wil
api_url = "http://api.disneyapi.dev/character"
# adres als je de volledige set karakters wil
api_url = "http://api.disneyapi.dev/character?page=&pageSize=10000"
# voor het request uit, sla het antwoord op in variabele "response"
response = requests.get(api_url)
# als response code aangeeft dat het gelukt is  ( code = 200 )
if response.status_code == 200:
    # pak dan de response JSON en houd bij in variabele "data"
    data = response.json()

    print("Lijst met Disney-personages:")
    # loop over alle personages in de lijst in variabele "data"
    for personage in data['data']:
        # houd de property 'name' bij in variabele "naam"
        naam = personage['name']
        # houd de property 'films' bij in variabele "films".   Opgelet !  hierin zit nu opnieuw een lijst !
        films = personage['films']
        #  als variabele "films" nu gevuld is  ( niet leeg is )
        if films:
            # vul variabele "oorspronkelijke_film" met de eerste uit de lijst
            oorspronkelijke_film = films[0]
        else:
            # de lijst van films kan ook leeg zijn, in dat geval vullen we variabele  "oorspronkelijke_film" met de tekst "Onbekend"
            oorspronkelijke_film = "Onbekend"
        # tenslotte alles verzamelen en afdrukken
        print(f"Naam: {naam} - Oorspronkelijke film: {oorspronkelijke_film}")

# als de response code aangeeft dat het niet gelukt is  ( niet 200 )
else:
    # foutmelding afdrukken
    print(f"Fout: {response.status_code} - {response.text}")