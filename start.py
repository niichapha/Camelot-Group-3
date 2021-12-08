from Great_hall import Great_hall
from action import action
from blacksmith import BlackSmith
from create_character import Create_character
from Library import library
from create_location import Create_location
from dialogue_class import Dialogue
from dialogue_func import message
from item_class import item
from item_func import item_creation

action('ShowMenu()')
action('Wait(3)')
action('HideMenu()')

#CREATE LOCATIONS)
lib = Create_location('lib', 'Library')
castle = Create_location('castle', 'GreatHall')
blacksmith = Create_location('blacksmith', 'Blacksmith')

# CREATE Charactors 
Evander=Create_character('Evander','D','Merchant', 'Spiky')
Merchant=Create_character('Merchant', 'D','Merchant', 'Spiky')
king=Create_character('king', 'D','king', 'Spiky')


# CREATE OBJECTS OR GLOBAL VARIABLES

library(Evander, lib)
Great_hall(Evander, king, castle)
BlackSmith(Evander, Merchant)

while(True):
    input()



