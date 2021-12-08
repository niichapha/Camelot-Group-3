from action import action
from create_item import item
from attack import attack
from Narration import Narration

def spooky_path(Evander,soldier):
    action('Enter('+Evander.name+', '+spooky_path.name+'.Well)')
    action('Enter('+soldier.name+', '+spooky_path.name+'.WestEnd)')
    Narration.Message('Evander',': I Know you are going to kill me')
    Narration.Message('Soldier',': Yes, I am. you are going to face the worst of time of your life')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    attack()


    




