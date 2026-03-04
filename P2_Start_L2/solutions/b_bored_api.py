# Gebruik de bored api om een JSON-bestand in te lezen: https://bored-api.appbrewery.com/random
# De response als json interpreteren kan zo: data = response.json()

import requests
import json

# spreek de bored API aan, houd het antwoord bij in variabele "response"
response = requests.get('https://bored-api.appbrewery.com/random')

# als de status_code van de response aangeeft dat het API verzoek gelukt is ( = 200 ) ...
if response.status_code == 200:
    # ...  dan halen we de JSON tekst eruit
    activity_data = response.json()
    # ...  en plukken uit de JSON de activity.
    activity = activity_data['activity']
    # die activity gaan we dan afdrukken
    print("Activiteit: ", activity)

    # bonus oefening:  om JSON mooi geformatteerd af te drukken kan je de "dumps" functie gebruiken uit de json library
    # eerst een lege lijn en aankondiging van de JSON
    print()
    print("hier komt de volledige JSON")
    #  dan de dumps functie gebruiken om de JSON te formatten en opslaan in variabele pretty_print
    pretty_print = json.dumps(activity_data, indent=4)
    # tenslotte afdrukken
    print(pretty_print)

#  als de code aangeeft dat er iets is mis gegaan:  tonen
else:
    print(f"Fout: {response.status_code} - {response.text}")