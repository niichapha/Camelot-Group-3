from action1 import action
from dialogues import dialogue_char 

def alchemist_shop():
	
	action('StopSound()')
	action('PlaySound(Serenity, Alchemy, True)')
	action('SetPosition(alchemist,Alchemy.BackDoor)')
	action('Enter(Evander, Alchemy.Door, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	dialogue_char('Evander: I want the Potions')
	dialogue_char('Alchemist: Which ones?')
	dialogue_char('I want a Blue, Red and Purple Potion')
	action('SetPosition(EnergyPotion,Alchemy.Bar.Left)')
	action('SetPosition(HealingPotion,Alchemy.Bar.Right)')
	action('SetPosition(FirePotion,Alchemy.Bar.Center)')
	action('Pickup(Evander, EnergyPotion,Alchemy.Bar.Left )')
	action('Pickup(Evander, HealingPotion,Alchemy.Bar.Right)')
	action('Pickup(Evander, FirePotion,Alchemy.Bar.Center)')
	action('Exit(Evander, Alchemy.Door, True)')



	
	
	
