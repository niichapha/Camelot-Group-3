from actioncomm import action
from dialogues import dialogue_char 

def blacksmith():
	action('StopSound()')
	action('PlaySound(Serenade, weap, True)')
	action('SetPosition(Merchant,weap.BackDoor)')
	action('Enter(Evander, weap.Door, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	dialogue_char('Evander: I want to buy a Weapon')
	dialogue_char('Merchant: Sure.')
	action('SetPosition(SwordOfHeisenberg,weap.Table.Right)')
	action('SetPosition(HammerOfHeisenberg,weap.Table.Left)')
	action('Pickup(Evander, SwordOfHeisenberg, weap.Table.Right)')
	action('Pickup(Evander, HammerOfHeisenberg, weap.Table.Left)')
	action('Exit(Evander,weap.Door,True')



