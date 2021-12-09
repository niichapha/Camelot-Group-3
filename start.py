#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

# This is the main file

from Great_hall import Great_hall
from action import action
from blacksmith import BlackSmith
from bridge import bridge_scene
from create_character import Create_character
from Library import library
from create_location import Create_location
from Narration import Narration
from create_item import item
from purplepotion import Hotel
from forestpath import forest_scene
from spookypath import spooky_path

action('ShowMenu()')
action('HideMenu()')

#CREATE LOCATIONS
lib = Create_location('lib', 'Library')
castle = Create_location('castle', 'GreatHall')
blacksmith = Create_location('blacksmith', 'Blacksmith')
hotel = Create_location('Hotel', 'Tavern')
forest_path=Create_location('forest','ForestPath')
bridge_path=Create_location('bridge','Bridge')
spooky_path=Create_location('spooky','SpookyPath')
dungeon=Create_location('dungeon','Dungeon')

# CREATE Characters 
Evander=Create_character('Evander','D','Merchant', 'Spiky') #composite element/ object
Merchant=Create_character('Merchant', 'D','Merchant', 'Spiky') #composite element/ object
king=Create_character('king', 'D','king', 'Spiky')
spy=Create_character('Spy', 'D', 'Bandit', 'Spiky')
enemy=Create_character('Enemy','D','Bandit','Spiky')
princessaida=Create_character('aida','A','Queen','Ponytail')
kingbodyguard=Create_character('bodyguard','D','HeavyArmour','Spiky')
soldier=Create_character('soldier','D','HeavyArmour','Spiky')

#-----------

#Create Messages 
message11= Narration('Evander', 'What abilities does this Sword give me?') #leaf elements/ object
message12 = Narration('Merchant', 'The Sword will increase your strength by 20%') #leaf elements/ object
message21 = Narration('Evander', 'Ok, What abilities does this Hammer give me?') #leaf elements/ object
message22 = Narration('Merchant', 'The Hammer will increase your strength by 10%') #leaf elements/ object

#-----------

# Calling location functions with parameters
library(Evander, lib)
Great_hall(Evander, king, castle)
BlackSmith(Evander, Merchant)
Hotel(Evander, spy, hotel)
forest_scene(Evander,enemy,forest_path)
spooky_path(Evander,soldier,dungeon)


#Using Composite Design Pattern
Evander.Message(message11)
Merchant.Message(message12)
Evander.Message(message21)
Merchant.Message(message22)


while(True):
    input()
