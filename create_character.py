# need to pass argument- name, body-type, clothing, 
# position and hairstyle in an order to create a character 

from action import action
from create_item import create_item

<<<<<<< HEAD
class Create_character:
=======
class Create_character: # created character class
>>>>>>> origin/beta_version2

    def __init__(self, name , body_style , clothing_style , hair="Spiky"):
        self.name = name
        action('CreateCharacter('+name+','+body_style+')')
        action('SetClothing('+name+', '+clothing_style+')')
        action('SetExpression('+name+',Happy)')
        action('SetHairStyle('+name+','+hair+')')