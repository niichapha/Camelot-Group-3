from action import action 

def Blacksmith_setup():
	
	# Start Background music for alchemy shop
	action('StopSound()')
	action('PlaySound(Serenity, WeaponShop, true)')
	
	action('Enter(Evander, WeaponShop.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('OpenFurniture(Evander, WeaponShop.Chest)')
	action('Pickup(Evander, SwordofHeisenberg, WeaponShop.Chest)')
	action('Exit(Evander, WeaponShop.Door, true)')
	action('EnableInput()')
