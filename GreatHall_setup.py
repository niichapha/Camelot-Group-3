from action import action 

def GreatHall_setup():
	
	action('StopSound()')
	action('PlaySound(Serenity, Alch, True)')
	
	action('Enter(Evander, GreatHall.Gate, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')

        action('SetExpression(King Heinrich, Happy)', False)
        action('Sit(King Heinrich, GreatHall.Throne)', False)

        
