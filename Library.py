from action import action
from create_item import item
from Narration import Narration


def library(Evander, lib):
    action('Enter('+Evander.name+', '+lib.name+'.Door')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    item.create_item('Spellbook', 'SpellBook', ''+lib.name+'.AlchemistTable')
    action('Pickup('+Evander.name+', Spellbook, '+lib.name+'.AlchemistTable)')
    action('Sit('+Evander.name+', '+lib.name+'.Chair)')
    Narration.Message('System', 'Please go to the castle to see your destiny')
    action('PutDown('+Evander.name+', Spellbook, '+lib.name+'.AlchemistTable)')
    action('SetPosition(Spellbook, '+lib.name+'.AlchemistTable)')
    action('Exit('+Evander.name+', '+lib.name+'.Door)')