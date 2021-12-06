from action import action

class Narration:
    def __init__(self,Name,dialogue):
        self.Name=Name
        self.dialogue=dialogue
<<<<<<< HEAD
    
=======

>>>>>>> origin/beta_version2
    def Message(Name, dialogue):
        action('SetNarration('+Name+': '+dialogue+')')
        action('ShowNarration')
        action('Wait(3)')
<<<<<<< HEAD
        action('HideNarration')
=======
        action('HideNarration')
>>>>>>> origin/beta_version2
