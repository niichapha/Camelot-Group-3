from actioncomm import action
from environment import create_places
from Characters import create_characters
from Library import library_setup
from GreatHall_setup import GreatHall_setup
from alchemist_shop_setup import alchemist_shop
from Blacksmith_setup import blacksmith
from item import Item


action('SetTitle(\"The Destiny\")')
action('ShowMenu()')
action('Wait(3)')

create_places()
create_characters()

action('HideMenu()')

library_setup()
GreatHall_setup()
alchemist_shop()
blacksmith()


while(True):
	input() 
