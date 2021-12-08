from typing import ItemsView
from action import action
from item_class import item
from item_func import item_creation
from dialogue_class import Dialogue
from dialogue_func import message

def BlackSmith(Evander, Merchant):
    action('SetPosition('+Merchant.name+', blacksmith.Anvil)')
    action('Enter('+Evander.name+', blacksmith.Door)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    message(''+Evander.name+'', 'Can I buy Weapons?')
    message(''+Merchant.name+'', 'Sure, Please select your choice')
    item_creation('SwordofHeisenberg', 'Sword', 'blacksmith.Table.Right')
    item_creation('HammerofHeisenberg', 'Hammer', 'blacksmith.Table.Left')
    action('Pickup(Evander, SwordofHeisenberg, blacksmith.Table)')
    action('Pickup(Evander, HammerofHeisenberg, blacksmith.Table)')