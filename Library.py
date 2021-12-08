from action import action
from create_item import create_item
from dialogue_class import Dialogue
from dialogue_func import message


def library(Evander, lib):
    action('Enter('+Evander.name+', '+lib.name+'.Door')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    create_item('Spellbook', 'SpellBook', ''+lib.name+'.AlchemistTable')
    action('Pickup('+Evander.name+', Spellbook, '+lib.name+'.AlchemistTable)')
    action('Sit('+Evander.name+', '+lib.name+'.Chair)')
    message('System','I have a mission for you')
    action('PutDown('+Evander.name+', Spellbook, '+lib.name+'.AlchemistTable)')
    action('SetPosition(Spellbook, '+lib.name+'.AlchemistTable)')
    action('Exit('+Evander.name+', '+lib.name+'.Door)')