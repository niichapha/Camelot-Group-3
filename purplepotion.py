from action import action
from create_item import item
from attack import attack
from Narration import Narration
from create_character import Create_character
from create_location import Create_location

Evander=Create_character('Evander','D','Merchant', 'Spiky')
spy=Create_character('Spy', 'D', 'Bandit', 'Spiky')
king=Create_character('king', 'D','king', 'Spiky')
hotel = Create_location('Hotel', 'Tavern')
castle = Create_location('castle', 'GreatHall')

def check_for_door():
    while True:
        received = input()
        if received == 'input east_exit city.Fountain':
            action('Exit(Evander, city.EastEnd)')
            action('Enter(Evander, Ruins.Exit)')
            action('SetCameraFocus(Evander)')
            action('SetCameraMode(follow)')
            item.create_item('Openscroll','OpenScroll', 'Ruins.Altar')
            action('WalkTo(Evander, Openscroll)')
            action('Take(Evander, Openscroll)')
            Narration.Message('System', 'This scroll contains the path to bar!')
            action('Exit(Evander, Ruins.Exit)')
            Hotel(Evander, spy, hotel)
            Castle(Evander, king, castle)
        elif received == 'input west_exit city.Fountain':
            action('Exit(Evander, city.WestEnd)')
            action('Enter(Evander, farm.Exit)')
            action('SetCameraFocus(Evander)')
            action('SetCameraMode(follow)')
            item.create_item('Redbook','RedBook', 'farm.Anvil')
            action('WalkTo(Evander, Redbook)')
            action('Take(Evander, Redbook)')
            Narration.Message('System', 'This book contains detailed map to find bar!')
            action('Exit(Evander, farm.Exit)')
            Hotel(Evander, spy, hotel)
            Castle(Evander, king, castle)


def Hotel(Evander, spy, hotel):
    #action('SetPosition('+Evander.name+', '+hotel.name+'.Door)')
    action('Enter('+Evander.name+', '+hotel.name+'.Door)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    action('Sit('+Evander.name+', '+hotel.name+'.BackLeftStool)')
    action('Enter('+spy.name+', '+hotel.name+'.Door)')
    action('Sit('+spy.name+', '+hotel.name+'.BackRightStool)')
    Narration.Message(''+Evander.name+'', 'I feel that you are spying me')
    Narration.Message(''+spy.name+'', 'May be, But wat can you do?')
    attack(''+Evander.name+'', ''+spy.name+'')
    action('Exit('+Evander.name+', '+hotel.name+'.Door)')

def city_place(Evander, city_location):
    action('Enter('+Evander.name+', '+city_location.name+'.NorthEnd)')
    action('SetCameraFocus('+Evander.name+')')
    action('SetCameraMode(follow)')
    action('EnableIcon(west_exit, exit, '+city_location.name+'.Fountain, "west_exit")')
    action('EnableIcon(east_exit, exit, '+city_location.name+'.Fountain, "East_exit")')
    action('EnableInput()')
    check_for_door()



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