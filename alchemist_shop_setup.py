from action import action 

def alchemist_shop_setup():
	
	action('StopSound()')
	action('PlaySound(Serenity, Alchemy, True)')
	action('Enter(Evander, Alchemy.Door, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	
	
	
