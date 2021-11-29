import time
from action import action
from master_action_controller import *
import global_game_states
from threading import Timer
from talk_controller import *
from add_clue import add_clue
from RedBranch_setup import RedBranch_setup

def RedBaranch_place(place):
    action('DisableInput()')
	action('WalkTo(Evander, ' + item + ')')
	action('Face(Evander, ' + item + ')')
	action('EnableInput()')

