from action import action
from create_item import create_item
from Narration import Message
from create_item import create_item


def BlackSmith(Evander, Merchant):
    action('SetPosition('+Merchant.name+', blacksmith.Anvil)')
    action('Enter('+Evander.name+', blacksmith.Door)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    Message('Evander', 'I want to buy a weapon')
    Message('Merchant', 'Sure')
    create_item('SwordofHeisenberg', 'Sword', 'blacksmith.Table.Right')
    create_item('HammerofHeisenberg', 'Hammer', 'blacksmith.Table.Left')
    action('Pickup(Evander, SwordofHeisenberg, blacksmith.Table)')
    action('Pickup(Evander, HammerofHeisenberg, blacksmith.Table)')