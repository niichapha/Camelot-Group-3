from action import action
from bridge_option1 import bridgeoption1
from Narration import Narration

class Revive(bridgeoption1):
    def revive_scene(Evander,princessaida):
        action('SetCameraFocus('+Evander.name+')')
        action('SetCameraMode(follow)')
        action('SetExpression('+Evander.name+', Sad)')
        Narration.Message('Evander',': Princess Aida, I am sorry! Please come back')
        action('Revive('+princessaida.name+')')
        action('SetExpression('+Evander.name+', happy)')
        action('SetExpression('+princessaida.name+', Sad)')
        










        

        




