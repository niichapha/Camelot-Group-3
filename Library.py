from action import action 

def library_setup():
	
	action('StopSound()')
	action('PlaySound(Serenity, Alch, True)')
	
	action('Enter(Evander, Library.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('Pickup(Evander, SpellBook)')
	action('PutDown(Evander, SpellBook,Library.Table)')
	action('Sit(Evander, Library.Chair)')
	action('EnableInput()')
	#jdhfdksufose;kdflsdk.v
