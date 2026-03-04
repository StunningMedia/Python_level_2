import requests

response = requests.get('https://official-joke-api.appspot.com/random_joke')
tekst = response.text
print(tekst)
# Deze file is voor de replit-gebruikers.
# Plak hier je oplossingen in om ze uit te voeren.