from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import PySimpleGUI as sg
import random

sets = Set.all()
set_names = []
for set in sets:
    set_names.append(set.name)
set_names.sort()
layout = [  [sg.Text('Welcome to MTG Set Viewer')],
            [sg.Text('Enter a set code to see all cards in that set or hit random for a random set'), sg.InputText()],
            [sg.Button('Enter'), sg.Button('Random')],
            [sg.Text("You can also select a set from this dropdown:")],
            [sg.Combo(set_names, default_value=set_names[0], readonly=True, s= (50, 22), k='-COMBO-'),
             sg.Button('Ok')],
            [sg.Output(size=(110,20))]]

window = sg.Window("MTG Set Viewer", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Random":
        sets = Set.all()
        random_set = random.choice(sets)
        cards = Card.where(set=random_set.code).all()
        for card in cards:
            print(card.name)
    elif event == "Enter":
        set_code = values[0]
        cards = Card.where(set=set_code).all()
        for card in cards:
            print(card.name)
    elif event == "Ok":
        dropdown_set = Set.where(name=values['-COMBO-']).all()
        for set in dropdown_set:
            if set.name == values['-COMBO-']:
                dropdown_code = set.code
                cards = Card.where(set=dropdown_code).all()
                for card in cards:
                    print(card.name)
window.close()
