# Bekijk de documentatie van de meme API: https://meme-api.com/gimme
# Roep de API aan en geef de afbeelding weer.
#
# Tip: Je kan de volgende import gebruiken.
# from PIL import Image
# from io import BytesIO

# !!! Hoewel je in de code van de module PIL importeert, installeer je daarvoor de module Pillow

# Tip: je kan van een response naar foto gaan met de volgende regels:
# image_data = BytesIO(response.content)
# image = Image.open(image_data)

import requests
from PIL import Image
from io import BytesIO
import json

# 1. Vraag een willekeurige meme op
api_url = "https://meme-api.com/gimme"
response = requests.get(api_url)

# als de response code aangeeft dat het gelukt is ( = 200 )
if response.status_code == 200:
    # pak dan de JSON uit de response en sla op in variabele "data"
    data = response.json()
    # haal het internet adres van de afbeelding op  ( property 'url' ) en sla op in variable "image_url"
    image_url = data["url"]

    # 2. Download de afbeelding
    #  met het net gevonden adres van de afbeelding doen we nu een nieuwe request, en slaan het antwoord op in variabele "img_response"
    img_response = requests.get(image_url)
    #  als de status code van image_response aangeeft dat het gelukt is  ( = 200 )
    if img_response.status_code == 200:
        # neem dan de INHOUD van img_response, maak daarmee een bytestream  ( functie 'BytesIO')
        #  en gebruikt die stream om te openen als afbeeling.  Houd de resulterende afbeelding bij in variabele "image"
        image = Image.open(BytesIO(img_response.content))
        # tenslotte nog de image tonen, met commando "show"
        image.show()                     # Toon de meme

    #  als de requst voor de image niet gelukt is  ( code niet 200 )
    else:
        # dan tonen we foutmelding:  downloaden niet gelukt
        print(f"Fout bij downloaden afbeelding: {img_response.status_code}")



    # bonus oefening:  om JSON mooi geformatteerd af te drukken kan je de "dumps" functie gebruiken uit de json library
    # eerst een lege lijn en aankondiging van de JSON
    print()
    print("hier komt de volledige JSON")
    #  dan de dumps functie gebruiken om de JSON te formatten en opslaan in variabele pretty_print
    pretty_print = json.dumps(data, indent=4)
    # tenslotte afdrukken
    print(pretty_print)

#  als de request naar de memes-API niet gelukt is  ( code niet 200 ) dan tonen we daarvoor de foutmelding
else:
    print(f"API-fout: {response.status_code} - {response.text}")