#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

from action import action
from blacksmith import BlackSmith
from create_character import Create_character
from begin_game import intro
from create_location import Create_location

action('ShowMenu()')
action('HideMenu()')

#CREATE LOCATIONS)
lib = Create_location('lib', 'Library')
blacksmith = Create_location('blacksmith', 'Blacksmith')
#-----------



# CREATE Charactors 
Evander=Create_character('Evander','D','Merchant','Castle', 'Spiky')
Merchant=Create_character('Merchant', 'D','Merchant','Castle', 'Spiky')
#-----------

# CREATE OBJECTS OR GLOBAL VARIABLES
#------------
intro(Evander)



while(True):
    input(Evander)