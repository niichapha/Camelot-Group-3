from action import action
from create_item import item
from Narration import Narration

def check_for_door():
    while True:
        received = input()
        if received == 'input east_exit city.BrownHouseDoor':
            action('Exit(Evander, city.BrownHouseDoor)')
            action('Enter(Evander, Ruins.Exit)')
            action('SetCameraFocus(Evander.name)')
            action('SetCameraMode(follow)')
            item.create_item('Openscroll','OpenScroll', 'Ruins.Altar')
            action('WalkTo(Evander, Openscroll)')
            action('Take(Evander, Openscroll)')
            Narration.Message('System', 'This scroll contains the path to bar!')
            action('Exit(Evander, Ruins.Exit)')


def city_place(Evander, city_location):
    action('SetPosition('+Evander.name+', '+city_location.name+')')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    action('EnableIcon(west_exit, exit, '+city_location.name+'.GreenHouseDoor, "west_exit")')
    action('EnableIcon(east_exit, exit, '+city_location.name+'.BrownHouseDoor, "East_exit")')
    action('EnableInput()')
    check_for_door()

    
