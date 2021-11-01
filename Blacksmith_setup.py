from action import action 

def Blacksmith_setup():
	
	# Start Background music for alchemy shop
	action('StopSound()')
	action('PlaySound(Serenity, WeaponShop, True)')
	
	action('Enter(Evander, WeaponShop.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('OpenFurniture(Evander, Camp.Chest)
	action('Pickup(Evander, Swords, WeaponShop.Chest)')
	action('Exit(Evander, WeaponShop.Door, true)')
	action('EnableInput()')
