#Задача №1. Кто самый умный супергерой? Есть API по информации о супергероях с информацией по всем супергероям.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.

import requests


def super_hero(hero):
    if (hero["name"] == "Hulk") or (hero["name"] == "Captain America") or (hero["name"] == "Thanos"):
        return True
    else:
        return False


response = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json', params=b'postId=1')
hero_dict = response.json()
out_filter = list(filter(super_hero, hero_dict))
max_int = out_filter[0]
for hero in out_filter:
    if hero["powerstats"]["intelligence"] > max_int["powerstats"]["intelligence"]:
        max_int = hero

print("Cамый умный супергерой: ", max_int["name"])