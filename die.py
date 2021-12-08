from action import action
from bridge import bridge
from bridge_option1 import bridgeoption1
from Narration import Narration
from attack import attack

class dieoption2(bridge):
    def die(king,princessaida):
        action('SetCameraFocus('+princessaida.name+')')
        action('SetCameraMode(follow)')
        action('PlaySound(Danger2, Bridge, true)')
        action('StopSound()')
        action('SetExpression('+king.name+', angry)')
        attack()






