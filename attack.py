from action import action

def attack(player_1 , player_2):
    action('WalkTo('+player_1+','+player_2+')')
    action('PlaySound(Draw)','False')
    action('Attack('+player_1+','+player_2+')')
    action('Die('+player_2+')')