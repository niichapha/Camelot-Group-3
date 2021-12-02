from action import action
from create_item import create_item
from Narration import Message

def Great_hall(Evander, king, castle):
    action('SetPosition('+king.name+', '+castle.name+'.Throne)')
    action('Sit('+king.name+', '+castle.name+'.Throne)')
    action('Enter('+Evander.name+', '+castle.name+'.Gate)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    action('WalkTo('+Evander.name+', '+king.name+')')
    action('SetExpression('+king.name+', happy)')
    Message(''+king.name+'', 'Good Morning '+Evander.name+'')
    Message(''+Evander.name+'', 'Good Morning your Highness')
    Message(''+king.name+'', 'I have a mission for you')
    Message(''+Evander.name+'', 'What is it your honour')
    Message(''+king.name+'', 'Please find princess Aida and kill her')
    action('SetExpression('+Evander.name+', angry)')
    Message(''+Evander.name+'', 'I am not doing that sorry')
    Message(''+king.name+'', 'It is my command')
    Message(''+Evander.name+'', 'Okay your honour')
    action('Exit('+Evander.name+', '+castle.name+'.Gate)')