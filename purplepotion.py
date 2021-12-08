from action import action
from create_item import item
from attack import attack
from Narration import Narration



def Hotel(Evander, spy, hotel):
    action('SetPosition('+Evander.name+', '+hotel.name+'.Door)')
    #action('Enter('+Evander.name+', '+hotel.name+'.Door)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    action('Sit('+Evander.name+', '+hotel.name+'.BackLeftStool)')
    action('Enter('+spy.name+', '+hotel.name+'.Door)')
    action('Sit('+spy.name+', '+hotel.name+'.BackRightStool)')
    Narration.Message(''+Evander.name+'', 'I feel that you are spying me')
    Narration.Message(''+spy.name+'', 'May be, But wat can you do?')
    attack(''+Evander.name+'', ''+spy.name+'')
