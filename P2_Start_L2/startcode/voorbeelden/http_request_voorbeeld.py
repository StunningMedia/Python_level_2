import requests

request = requests.get('https://api.github.com/events')
tekst = request.text