# Print de response van deze joke api:https://official-joke-api.appspot.com/random_joke
# Kijk naar het http_request voorbeeld om te zien hoe het moet.

import requests

#  spreek de joke API aan, houd het antwoord bij in variabele "response"
response = requests.get('https://official-joke-api.appspot.com/random_joke')


# - Als de response code gelijk is aan 200, print de response text
if response.status_code == 200:
    print(response.text)
# - Bij andere codes een foutmelding geprint wordt. (Wees creatief met je foutcodes).
else:
    print("418 I'm a teapot")