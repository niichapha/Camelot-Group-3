from action import action
from Narration import Narration
from create_item import item
from create_location import Create_location
from create_character import Create_character
from purplepotion import *

city_location=Create_location('city', 'City')
Evander=Create_character('Evander','D','Merchant', 'Spiky')

def check_for_potion():
    while True:
        received = input()
        if received == 'input potion Purplepotion':
            action('Exit(Evander, Alchemy.Door)')
            city_place(Evander, city_location)
            break

def alchemy():
    action('Enter(Evander, Alchemy.Door)')
    action('SetCameraFocus(Evander)')
    action('SetCameraMode(follow)')
    item.create_item('Purplepotion', 'PurplePotion', 'Alchemy.AlchemistTable.Left')
    item.create_item('Redpotion', 'RedPotion', 'Alchemy.AlchemistTable.Right')
    action('WalkTo(Evander, Alchemy.AlchemistTable)')
    action('EnableIcon(potion, potion, Purplepotion, "PurplePotion")')
    action('EnableIcon(potion, potion, Redpotion, "RedPotion")')
    action('EnableInput()')
    check_for_potion()

