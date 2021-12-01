from Narration import Narration
from actioncomm import action_command

class Narration_methods(Narration):
    def __init__(self,name,dialogue):
        self.name=name
        self.dialogue=dialogue
        def sub_dialoge():
            action_command('SetDialog('+name+','+dialogue+')')
            action_command('ShowDialog()')
            action_command('Wait(3)')
            action_command('HideDialog()')

nar=Narration_methods()


