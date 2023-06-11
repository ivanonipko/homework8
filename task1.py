from pprint import pprint
import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
heros_responce = requests.get(url)
heros = heros_responce.json()
names = ["Hulk", "Captain America", "Thanos"]
max_intelligence = 0
max_intelligence_hero = {}
for hero in heros:
    if hero["name"] in names and hero["powerstats"]["intelligence"] > max_intelligence:
        max_intelligence = hero["powerstats"]["intelligence"]
        max_intelligence_hero = hero
pprint(max_intelligence_hero["name"] )
