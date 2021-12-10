#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

# This is the main file

from Great_hall import Great_hall
from action import action
from blacksmith import BlackSmith
from bridge import bridge
from create_character import Create_character
from Library import library
from create_location import Create_location
from Narration import Narration
from create_item import item
from purplepotion import Castle, Hotel
from forestpath import forest_scene
from spookypath import spooky_path

action('ShowMenu()')
action('Wait(3)')
action('HideMenu()')

#CREATE LOCATIONS)
lib = Create_location('lib', 'Library')
castle = Create_location('castle', 'GreatHall')
blacksmith = Create_location('blacksmith', 'Blacksmith')
hotel = Create_location('Hotel', 'Tavern')

# CREATE Charactors 
Evander=Create_character('Evander','D','Merchant', 'Spiky') 
Merchant=Create_character('Merchant', 'D','Merchant', 'Spiky') 
king=Create_character('king', 'D','king', 'Spiky')
spy=Create_character('Spy', 'D', 'Bandit', 'Spiky')
forest_path=Create_location('forest','ForestPath')
bridge_path=Create_location('bridge','Bridge')
spooky_path=Create_location('spooky','SpookyPath')
dungeon=Create_location('dungeon','Dungeon')

#-----------

# CREATE Characters 
Evander=Create_character('Evander','D','Merchant', 'Spiky')  #composite element/ object
Merchant=Create_character('Merchant', 'D','Merchant', 'Spiky')  #composite element/ object
king=Create_character('king', 'D','king', 'Spiky') 
enemy=Create_character('Enemy','D','Bandit','Spiky')
princessaida=Create_character('aida','A','Queen','Ponytail')
kingbodyguard=Create_character('bodyguard','D','HeavyArmour','Spiky')
soldier=Create_character('soldier','D','HeavyArmour','Spiky')
#-----------


# Calling location functions with parameters
# library(Evander, lib)
# Great_hall(Evander, king, castle)
# BlackSmith(Evander, Merchant)
Hotel(Evander, spy, hotel)
Castle(Evander, king, castle)
# forest_scene(Evander,enemy,forest_path)
# spooky_path(Evander,soldier,dungeon)


while(True):
    input()
