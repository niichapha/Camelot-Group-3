from actioncomm import action 
from dialogues import dialogue_char

def GreatHall_setup():
	action('StopSound()')
	action('Enter(Evander, castle.Gate, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	action('Enter(King_Heinrich,  castle.Gate, true)')
	action('SetExpression(King_Heinrich, happy)')
	action('Sit(King_Heinrich, castle.Throne)')
	dialogue_char("King: Good Morning Evander")
	dialogue_char("Evander: Good Morning your Highness")
	dialogue_char("King: I have a mission for you")
	dialogue_char("Evander: What is it your honour?")
	dialogue_char("King: Please find Princess Aida and Kill her")
	action('SetExpression(Evander, angry)')
	dialogue_char("Evander: I am not doing that. I am sorry")
	dialogue_char("King: It is my command")
	dialogue_char("King: I feel the lady will kill my life. SO, I want you to kill her")
	dialogue_char("Evander: But, it is against my ethics. I wont do it")
	dialogue_char("King: You have to do it no matter what")
	dialogue_char("Evander: Okay, I will do it")
	action('Exit(Evander, castle.Gate, true)')

	
