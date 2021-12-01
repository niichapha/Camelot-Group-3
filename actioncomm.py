from check_for_success import check_for_success
from action import action_game

def action(command,wait=True):
    print('start ' + command)
    if wait==True:
        return check_for_success(command)
    else:
        return True