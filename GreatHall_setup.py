from action1 import action 
from dialogues import dialogue_char

def GreatHall_setup():
	action('StopSound()')
	action('PlaySound(Serenity, Alch, True)')
	action('Enter(Evander, GreatHall.Gate, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	action('Enter(King_Heinrich, GreatHall.Gate, true)')
	action('SetExpression(King_Heinrich, happy)', False)
	action('Sit(King_Heinrich, GreatHall.Throne)', False)
	dialogue_char("King: Good Morning Evander")
	dialogue_char("Evander: Good Morning your Higheness")
	dialogue_char("King: I have a mission for you")
	dialogue_char("Evander: What is it your honour?")
	dialogue_char("King: Please find Princess Aida and Kill her")
	action('SetExpression(Evander, angry)', False)
	dialogue_char("Evander: I am not doing that. I am sorry")
	dialogue_char("King: It is my command")
	dialogue_char("Evander: Okay your honour")
	action('Exit(Evander, GreatHall.Gate, true)')
	
