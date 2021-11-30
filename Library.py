from action1 import action 
def library_setup():
	action('StopSound()')
	action('PlaySound(Serenity, Alch, True)')
	action('Enter(Evander, lib.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('Pickup(Evander, SpellBook)')
	action('Sit(Evander, lib.Chair)')
	action('SetNarration(Please go to the Castle to see your Destiny!)')
	action('PutDown(Evander, SpellBook,lib.Table)')
	action('EnableInput()')

