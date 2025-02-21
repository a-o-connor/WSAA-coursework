#Libraries
import requests
import json

shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1" 
shuffle = requests.get(shuffle_url)
deck_id = shuffle.json()["deck_id"]

number_of_cards = 2
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={number_of_cards}"
drawn_cards = requests.get(draw_url).json()

for i in range(number_of_cards):
    card=drawn_cards["cards"][i]
    value=card['value']
    suit=card["suit"]
    print(f"{value} OF {suit}")