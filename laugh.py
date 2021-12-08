from action import action
from bridge import bridge

class laugh(bridge):
    def laugh_scene(Evander,princessaida):
        action('SetCameraFocus('+Evander.name+')')
        action('SetCameraMode(follow)')
        action('Laugh('+Evander.name+')')
        action('Laugh('+princessaida.name+')')
        action('CreateEffect(bridge, Explosion)')
        action('EnableEffect(bridge, Explosion)')
        action('Wait(3)')
        action('DisableEffect(bridge, Explosion)')
        action('Die('+Evander.name+')')
        action('Die('+princessaida.name+')')








