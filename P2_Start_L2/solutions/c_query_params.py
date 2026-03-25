# Maak een programma dat:
# - De naam van de gebruiker vraagt.
# - De naam van de gebruiker doorstuurt naar de API.
# - Een tekstje print met de naam en de voorspelde leeftijd.

import requests
# vraag de naam van de gebruiker
naam = input("Geef jouw naam: ")

# vorm het request met de correcte parameter, en houd het antwoord bij in variabele "response"
response = requests.get(
    url="https://api.agify.io/",
    params={
        "name": naam,
        "country_id":"NL"
    }
)

#  als de response code aangeeft dat het gelukt is   (  = 200 )
if response.status_code == 200:
    # pak dan de JSON uit de response en sla op in variabele "data"
    data = response.json()
    # haal dan de leeftijd uit de JSON data  ( property 'age' ) en sla op in variabele "leeftijd"
    leeftijd = data['age']
    # verzamel het geheel en druk af
    print(f"{naam} is vermoedelijk  {leeftijd} jaar oud.")
#  als de code aangeeft dat het niet gelukt is, druk een foutmelding af
else:
    print("Ooops! Probeer het later opnieuw.")