import time
from action import action
from master_action_controller import *
import global_game_states
from threading import Timer
from talk_controller import *
from add_clue import add_clue
from alchemist_shop_setup import alchemist_shop_setup

def inspect_item(item) : 
    action('DisableInput()')
	action('WalkTo(Evander, ' + item + ')')
	action('Face(Evander, ' + item + ')')
	action('EnableInput()')

    if item == 'HealingPotion':
        midscene_narration('The label reads- Healing Potion.')
        action('PlaySound(Unlock, HealingPotion, false')
    
    elif item == 'ResurrectPotion':
        midscene_narration('The label reads- Resurrect Potion.')
        actiion('PlaySound(Unlock, ResurrectPotion, false')
    
    elif item == 'EnergyPotion':
        midscene_narration('The label reads- Energy Potion.')
        action('PlaySound(Unlock, EnergyPotion, false)')

        player_response = 'input Selected AllPotionsList'
        if player_response == 'Input Selected AllPotionsList':
            while player_response!= 'Input Selected Done':
                player_response =  set_dialog('We offer One blue potion: Healing Potion \\n[Blue| HealingPotion]\\n[AllPotionsList | Back]', ['Blue', 'AllPotionsList'])
                if player_response == 'input Selected Blue':
                    player_response = set_dialog('Healing Potion: This can increase your health by 50%. Also known as Elixer. \\n[Back | Back]', ['Back']))
        
        elif player_response == 'Input Selected AllPotionsList':
            while player_response!= 'Input Selected Done':
                player_response =  set_dialog('We offer One Red potion: Resurrect Potion \\n[Red| ResurrectPotion]\\n[AllPotionsList | Back]', ['Red', 'AllPotionsList'])
                if player_response == 'input Selected Red':
                    player_response = set_dialog('Resurrect Potion: This can revive someone. Also known as Resurgence. \\n[Back | Back]', ['Back']))


        elif player_response == 'Input Selected AllPotionsList':
            while player_response!= 'Input Selected Done':
                player_response =  set_dialog('We offer One Purple potion: Energy Potion \\n[Purple| EnergyPotion]\\n[AllPotionsList | Back]', ['Purple', 'AllPotionsList'])
                if player_response == 'input Selected Purple':
                    player_response = set_dialog('Energy Potion: This can increase your energy by 50%. Also known as Vehemence. \\n[Back | Back]', ['Back']))


            action('HideDialog()')
		    action('PlaySound(Danger1, AlchemyShop, false')


    def alchemist_shop_controller:
        alchemist_shop_setup()
        while global_game_states.current_scene == 'alachemist_shop' and global_game_states.potions =='':
            received = input()
            if received.startswith('input inspect'):
                received = received.split(' ')
                item = received[2]
                inspect_item(item)
            elif recieved.startswith('input Leave'):
                global_game_states.current_scene = 'city'
                global_game_states.prev_scene = 'alchemist_shop'

            else:

                check_master_action(received)
