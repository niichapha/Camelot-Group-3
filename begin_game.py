from action import action
from create_item import create_item
from Narration import Message



def attack(player_1 , player_2):
    action('WalkTo('+player_1+','+player_2+')')
    action('PlaySound(Draw)','False')
    action('Attack('+player_1+','+player_2+')')
    action('Die('+player_2+')')

def intro(Evander):
    action('Enter(Evander, lib.Door, True)')
    action('SetCameraFocus(Evander)')
    action('SetCameraMode(follow)')
    action('CreateItem(Spellbook, SpellBook)')
    action('SetPosition(Spellbook, lib.AlchemistTable)')
    action('Pickup(Evander, Spellbook, lib.AlchemistTable)')
    action('Sit(Evander, lib.Chair)')
    Message('System', 'Please go to the castle to see your destiny')
    action('PutDown(Evander, Spellbook, lib.AlchemistTable)')
    #action('EnableInput()')
    action('Exit(Evander, lib.Door)')
    action('SetPosition(Merchant, blacksmith.Anvil')
    action('Enter(Evander, blacksmith.Door)')
    action('SetCameraFocus(Evander)')
    action('SetCameraMode(follow)')
    Message('Evander', 'I want to buy a weapon')
    Message('Merchant', 'Sure')
    action('CreateItem(SwordofHeisenberg, Sword)')
    action('CreateItem(HammerofHeisenberg, Hammer)')
    action('SetPosition(SwordofHeisenberg, blacksmith.Table.Right)')
    action('SetPosition(HammerofHeisenberg, blacksmith.Table.Left)')
    action('Pickup(Evander, SwordofHeisenberg, blacksmith.Table)')
    action('Pickup(Evander, HammerofHeisenberg, blacksmith.Table)')