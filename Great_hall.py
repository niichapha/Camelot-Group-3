from action import action
from create_item import item
from Narration import Narration

def Great_hall(Evander, king, castle): #Enabled Input
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
    Narration.Message(''+king.name+'', 'I have a mission for you')
    Narration.Message(''+Evander.name+'', 'What is it your honour')
    Narration.Message(''+king.name+'', 'Please find princess Aida and kill her')
    action('SetExpression('+Evander.name+', angry)')
    Narration.Message(''+Evander.name+'', 'I am not doing that sorry')
    Narration.Message(''+king.name+'', 'It is my command')
    Narration.Message(''+Evander.name+'', 'Okay your honour')
    action('Exit('+Evander.name+', '+castle.name+'.Gate)')