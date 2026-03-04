# Bekijk de documentatie voor de free games API: https://www.freetogame.com/api-doc
# Hoe zou je een lijst met games kunnen binnenhalen met de volgende voorwaarden?
# - PC-games
# - Gesorteerd volgens relevantie

# Bijkomende opdracht:
# Print voor alle pc-games die het woord “world” bevatten, de titel en de game_url.
# Zorg dat het niet gevoelig is aan hoofdletters.

import requests
import json

#  vorm een request, naar de juiste URL en met de juiste parameters, sla het antwoord op in variabele "response"
response = requests.get(
    url="https://www.freetogame.com/api/games",
    params={
        'platform': 'pc',
        'sort-by': 'relevance'
    }
)

#  als de response code aangeeft dat het gelukt is  ( = 200 )
if response.status_code == 200:
    # pak dan de JSON van de response en sla op in variabele "game_data"
    game_data = response.json()
    # loop over alle games in game_data
    for game in game_data:
        # en als de titel van de game  ( property 'title' ) het woord "world' bevat
        # (om problemen met hoofdletter/kleine letter te vermijden zetten we eerst de inhoud van 'title' om naar lowercase
        if "world" in game['title'].lower():
            #  dan alles verzamelen en afdrukken
            print(f"{game['title']}: {game['game_url']}")



    # bonus oefening:  om JSON mooi geformatteerd af te drukken kan je de "dumps" functie gebruiken uit de json library
    # eerst een lege lijn en aankondiging van de JSON
    print()
    print("hier komt de volledige JSON")
    #  dan de dumps functie gebruiken om de JSON te formatten en opslaan in variabele pretty_print
    pretty_print = json.dumps(game_data, indent=4)
    # tenslotte afdrukken
    print(pretty_print)

# als de code aangeeft dat er iets is misgegaan, toon dan de foutmelding
else:
    print(f"Fout: {response.status_code} - {response.text}")