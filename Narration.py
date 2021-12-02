from action import action

class Narration:
    def __init__(self,Name,dialogue):
        self.Name=Name
        self.dialogue=dialogue

def Message(Name, dialogue):
    action('SetNarration('+Name+': '+dialogue+')')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')