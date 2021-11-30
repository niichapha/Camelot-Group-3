from action1 import action 
from dialogues import dialogue_char

def GreatHall_setup():
	action('StopSound()')
	action('Enter(Evander, Castle.Gate, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	action('Enter(King_Heinrich,  Castle.Gate, true)')
	action('SetExpression(King_Heinrich, happy)')
	action('Sit(King_Heinrich, Castle.Throne)')
	dialogue_char("King: Good Morning Evander")
	dialogue_char("Evander: Good Morning your Highness")
	dialogue_char("King: I have a mission for you")
	dialogue_char("Evander: What is it your honour?")
	dialogue_char("King: Please find Princess Aida and Kill her")
	action('SetExpression(Evander, angry)')
	dialogue_char("Evander: I am not doing that. I am sorry")
	dialogue_char("King: It is my command")
	dialogue_char("Evander: Okay your honour")
	action('Exit(Evander, Castle.Gate, true)')

	
