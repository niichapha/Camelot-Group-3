from action import action 

def Blacksmith_setup():
	
	# Start Background music for alchemy shop
	action('StopSound()')
	action('PlaySound(Serenity, Alch, True)')
	
	action('Enter(Evander, Blacksmith.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('Pickup(Evander, Sword, Blacksmith.Table)')
	action('Exit(Evander, Blacksmith.Door, true)')
	action('EnableInput()')
