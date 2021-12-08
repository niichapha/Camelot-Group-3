from action import action

class Narration:
    def __init__(self,Name,dialogue):
        self.Name=Name
        self.dialogue=dialogue

    def Message(Name, dialogue):
        action('SetDialog('+Name+': '+dialogue+')')
        action('ShowDialog()')
        action('Wait(3)')
        action('HideDialog()')
