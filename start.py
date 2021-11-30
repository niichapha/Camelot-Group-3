from action1 import action
from environment import create_places
from Characters import create_characters
from Library import library_setup
from GreatHall_setup import GreatHall_setup
from alchemist_shop_setup import alchemist_shop
from Blacksmith_setup import blacksmith


action('SetTitle(\"The Destiny\")')
action('ShowMenu()')
action('HideMenu()')
create_places()
create_characters()

action('CreateItem(EnergyPotion, PurplePotion)')
action('CreateItem(HealingPotion,BluePotion)')
action('CreateItem(FirePotion, RedPotion)')
action('CreateItem(SwordOfHeisenberg, Sword)')
action('CreateItem(HammerOfHeisenberg, Hammer)')

library_setup()
GreatHall_setup()
alchemist_shop()
blacksmith()


action('Wait(5s)')
action('HideDialog()')



action('SetExpression(Evander, Angry)')

while(True):
	input() 
