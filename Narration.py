from actioncomm import action_command
class Narration:
    class __init__(self,name,dialogue):
        self.name=name
        self.dialogue=dialogue
        action_command('SetNarration('+name+','+dialogue+')')
        action_command('ShowNarration()')
        action_command('Wait(3)')
        action_command('HideNarration()')





