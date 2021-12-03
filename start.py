#This is the Starting point of the story. 
# Configure this file in your startExperienceManager file
# Try not to logic in this file except importing files.(should follow modularized coding practice)

# This is the main file

from Great_hall import Great_hall
from action import action
from blacksmith import BlackSmith
from create_character import Create_character
from Library import library
from create_location import Create_location
from Narration import Narration
from create_item import item
from Narration import Message

action('ShowMenu()')
action('Wait(3)')
action('HideMenu()')

#CREATE LOCATIONS)
lib = Create_location('lib', 'Library')
castle = Create_location('castle', 'GreatHall')
blacksmith = Create_location('blacksmith', 'Blacksmith')
#-----------

#Create Messages 
message11= Narration('Evander', 'What abilities does this Sword give me?') #leaf elements/ object
message12 = Narration('Merchant', 'The Sword will increase your strength by 20%') #leaf elements/ object
message21 = Narration('Evander', 'Ok, What abilities does this Hammer give me?') #leaf elements/ object
message22 = Narration('Merchant', 'The Hammer will increase your strength by 10%') #leaf elements/ object

# CREATE Charactors 
Evander=Create_character('Evander','D','Merchant', 'Spiky')  #composite element/ object
Merchant=Create_character('Merchant', 'D','Merchant', 'Spiky')  #composite element/ object
king=Create_character('king', 'D','king', 'Spiky') 
#-----------

# CREATE OBJECTS OR GLOBAL VARIABLES
#------------
library(Evander, lib)
Great_hall(Evander, king, castle)
BlackSmith(Evander, Merchant)

#Using Composite Design Pattern
Evander.Message(message11)
Merchant.Message(message12)
Evander.Message(message21)
Merchant.Message(message22)


while(True):
    input()
