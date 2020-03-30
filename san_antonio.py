#-*- coding: utf8 -*-
import random
import json

# Give a Json file and return a List
def read_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values

def message(character, quote):
    return "{} a dit : '{}'".format (character, quote)

def random_item(my_list):
    rand_numb = random.randint(0, len(my_list) - 1) #get random number
    return my_list[rand_numb]

def random_character():
    all_values = read_from_json("../characters.json", "character")
    return random_item(all_values)

def random_quote():
    all_values = read_from_json("../quotes.json", "quote")
    return random_item(all_values)

#Program

print("---------------")
print("Hello, World !")
print("---------------")

user_answer = input("Appuyez sur la touche Entrée pour afficher une citation ou appuyez sur B pour quitter l'application.")

while user_answer != "b":
    print(message(random_character(), random_quote()))
    user_answer = input("Appuyez sur la touche Entrée pour afficher une citation ou appuyez sur B pour quitter l'application.")
