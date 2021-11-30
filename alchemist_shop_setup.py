from action1 import action
from dialogues import dialogue_char 

def alchemist_shop():
	
	action('StopSound()')
	action('PlaySound(Serenity, alchemy, True)')
	action('SetPosition(alchemist,alchemy.BackDoor)')
	action('Enter(Evander, alchemy.Door, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	dialogue_char('Evander: I want the Potions')
	dialogue_char('Alchemist: Which ones?')
	dialogue_char('I want a Blue, Red and Purple Potion')
	action('SetPosition(EnergyPotion,alchemy.Bar.Left)')
	action('SetPosition(HealingPotion,alchemy.Bar.Right)')
	action('SetPosition(FirePotion,alchemy.Bar.Center)')
	action('Pickup(Evander, EnergyPotion,alchemy.Bar.Left )')
	action('Pickup(Evander, HealingPotion,alchemy.Bar.Right)')
	action('Pickup(Evander, FirePotion,alchemy.Bar.Center)')
	action('Exit(Evander, alchemy.Door, True)')



	
	
	
