from action import action 

def Blacksmith_setup():
	
	# Start background music for blacksmith shop
	action('StopSound()')
	action('PlaySound(Serenade, WeaponShop, True)')
	action('Enter(Evander, WeaponShop.Door, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')