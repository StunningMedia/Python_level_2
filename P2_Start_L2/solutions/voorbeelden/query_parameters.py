import requests

response = requests.get(
    url=f"https://cataas.com/cat/says/poes",
    params={"fontColor": "blue"}
)