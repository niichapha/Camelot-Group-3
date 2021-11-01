import global_states
from action import action


def add_clue(clue, clue_item):
	
	if [clue_item, clue] not in global_states.current_clues:
		global_states.current_clues.append([clue_item, clue])
		action('EnableIcon(ClueRead, Book,' + clue_item + ', Read Clue, true)')
		if global_states.current_scene == 'hallway':
			global_states.castle_clues.append([clue_item, clue])
		elif global_states.current_scene == 'alchemist_shop':
			global_states.alchemist_shop_clues.append([clue_item, clue])
		elif global_states.current_scene == 'blacksmith_shop':
			global_states.blacksmith_shop_clues.append([clue_item, clue])