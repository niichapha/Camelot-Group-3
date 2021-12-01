from action1 import action 
def library_setup():
	action('StopSound()')
	action('PlaySound(Serenity, bookplace, True)')
	action('Enter(Evander, bookplace.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('Set(Spell, bookplace.Table)')
	action('Pickup(Evander, Spell)')
	action('Sit(Evander, bookplace.Chair)')
	action('SetNarration(Please go to the Castle to see your Destiny!)')
	action('PutDown(Evander, Spell,bookplace.Table)')
	action('EnableInput()')

