from dialogue_class import Dialogue
from action import action

def message(char_name,dialogue):
    action('SetDialog('+char_name+','+dialogue+')')
    action('ShowDialog()')
    action('Wait(3)')
    action('HideDialog()')

dialogue_obj=Dialogue()
dialogue_obj.message()
