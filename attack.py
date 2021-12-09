from action import action

def attack(player_1 , player_2):
    action('WalkTo('+player_1+','+player_2+')')
    action('Draw('+player_1+',SwordofHeisenberg)')
    action('PlaySound(Draw)','False')
    action('Attack('+player_1+','+player_2+')')
    action('PlaySound(Attack1)','False')
    action('PlaySound(Death1)','False')
    action('CreateEffect('+player_2+',Blood)')
    action('Die('+player_2+')')
    