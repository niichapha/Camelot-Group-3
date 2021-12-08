from action import action
from create_item import item
from Narration import Narration


def BlackSmith(Evander, Merchant):
    action('SetPosition('+Merchant.name+', blacksmith.Anvil)')
    action('Enter('+Evander.name+', blacksmith.Door)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    Narration('Evander', 'I want to buy a weapon')
    Narration('Merchant', 'Sure')
    item.create_item('SwordofHeisenberg', 'Sword', 'blacksmith.Table.Right')
    item.create_item('HammerofHeisenberg', 'Hammer', 'blacksmith.Table.Left')
    action('Pickup(Evander, SwordofHeisenberg, blacksmith.Table)')
    action('Pickup(Evander, HammerofHeisenberg, blacksmith.Table)')