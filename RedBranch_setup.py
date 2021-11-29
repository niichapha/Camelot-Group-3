from action import action

def RedBranch_setup():

	action('StopSound()')
	action('PlaySound(Attack1, Azkaban , True)')
	action('Enter(Evander, Azkaban.Door, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')

    action('StopSound()')
	action('PlaySound(River, PortNebula, True)')
	action('Enter(Evander, PortNebula.Exit, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')


    action('StopSound()')
	action('PlaySound(Serenade, CampMilitar, True)')
	action('Enter(Evander, CampMilitar.Door, True)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')


