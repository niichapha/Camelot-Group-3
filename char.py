from action1 import action

class Char:
    def __init__(self,name,cloth,body,hair='Spiky'):
        self.name = name
        action('CreateCharacter('+name+','+body+')')
        action('SetClothing('+name+', '+cloth+')')
        action('SetHairStyle('+name+','+hair+')')