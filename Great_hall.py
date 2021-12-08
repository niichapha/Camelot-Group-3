from action import action 
from dialogue_class import Dialogue
from dialogue_func import message

def Great_hall(Evander, king, castle):
    action('SetPosition('+king.name+', '+castle.name+'.Throne)')
    action('Sit('+king.name+', '+castle.name+'.Throne)')
    action('Enter('+Evander.name+', '+castle.name+'.Gate)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    action('EnableInput()')
    #action('WalkTo('+Evander.name+', '+king.name+')')
    action('SetExpression('+king.name+', happy)')
    action('SetExpression('+Evander.name+', happy)')
    message(''+king.name+'', 'Good Morning '+Evander.name+'')
    message(''+Evander.name+'', 'Good Morning your Highness')
    message(''+king.name+'', 'I have a mission for you')
    message(''+Evander.name+'', 'What is it your honour')
    message(''+king.name+'', 'Please find princess Aida and kill her')
    action('SetExpression('+Evander.name+', angry)')
    message(''+Evander.name+'', 'I am not doing that sorry')
    message(''+king.name+'', 'It is my command')
    message(''+Evander.name+'', 'Okay your honour')
    action('Exit('+Evander.name+', '+castle.name+'.Gate)')