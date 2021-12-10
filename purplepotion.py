from action import action
from create_item import item
from attack import attack
from Narration import Narration


def Ruins(Evander, Ruins):
    action('SetPosition('+Evander.name+', '+Ruins.name+')')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    item.create_item('Openscroll','OpenScroll', ''+Ruins.name+'.Altar')
    action('WalkTo('+Evander.name+', Openscroll)')


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
    action('Exit('+Evander.name+', '+hotel.name+'.Door)')

def Castle(Evander, king, castle):
    action('SetPosition('+king.name+', '+castle.name+'.Throne)')
    action('Sit('+king.name+', '+castle.name+'.Throne)')
    action('Enter('+Evander.name+', '+castle.name+'.Gate)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
    action('WalkTo('+Evander.name+', '+king.name+')')
    action('SetExpression('+king.name+', happy)')
    Narration.Message(''+king.name+'', 'Good Morning '+Evander.name+'')
    Narration.Message(''+Evander.name+'', 'Good Morning your Highness')
    Narration.Message(''+king.name+'', 'What makes you come here again?')
    Narration.Message(''+Evander.name+'', 'I know you sent a soldier to spy on me')
    Narration.Message(''+king.name+'', 'So i think you understood what i can do!')
    action('SetExpression('+Evander.name+', angry)')
    attack(''+Evander.name+'', ''+king.name+'')
    action('Exit('+Evander.name+', '+castle.name+'.Gate)')