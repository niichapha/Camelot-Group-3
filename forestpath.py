from Narration import Narration
from action import action
from attack import attack
from create_character import Create_character

def forest_scene(Evander,enemy,forest_path):
    action('Enter('+Evander.name+', '+forest_path.name+'.EastEnd)')
    action('Enter('+enemy.name+', '+forest_path.name+'.WestEnd)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    Narration.Message('Evander',': Who are you? What do you want?')
    Narration.Message('Enemy',': I want your life')
    Narration.Message('Evander',': What do you mean?')
    Narration.Message('Enemy',':I was asked to kill you')
    Narration.Message('Evander',':By whom?')
    Narration.Message('Enemy',':I am not allowed to disclose it to you')
    action('Wait(1)')
    attack()
    action
    

    
