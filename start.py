from action1 import action
from environment import create_places
from Characters import create_characters


action('SetTitle(\"The Destiny\")')
action('ShowMenu()')
action('HideMenu()')
create_places()
create_characters()


action('CreateItem(EnergyPotion, PurplePotion)')
action('CreateItem("HealingPotion",BluePotion)')
action('CreateItem("FirePotion", RedPotion)')

action('StopSound()')
action('PlaySound(Serenity, BookPlace, True)')
action('Enter(Evander, BookPlace.Door, true)')
action('EnableInput()')
action('SetCameraFocus(Evander)')
action('SetCameraMode(follow)')
#action('SetItem(SpellBook, GreenBook)')
#action('Pickup(Evander, SpellBook)')
#action('PutDown(Evander, SpellBook, BookPlace.Table)')
action('SetNarration("Pickup the book on the table.")')
action('ShowNarration()')
action('Sit(Evander, BookPlace.Chair)')
action('HideNarration()')
action('Exit(Evander, BookPlace.Door)')
action('StopSound()')

action('PlaySound(Serenity, Castle, True)')	
action('Enter(Evander, Castle.Gate, true)')
action('SetCameraFocus(Evander)')
action('SetCameraMode(follow)')
action('Enter(King Heinrich, Castle.LeftDoor)')
action('WalkTo(King Heinrich, Castle.Throne)')
action('Sit(King Heinrich, Castle.Throne)')
action('SetLeft(King Heinrich)')
action('SetRight(Evander)') 
action('SetExpression(King Heinrich, Happy)')
action('SetDialog("King Heinrich: Welcome Evander")')
action('ShowDialog()')
action('SetDialog("It has been a long time")')
action('ShowDialog()')
action('SetDialog("Evander: What do you want from me now, I am not here to do any filthy business of yours")')
action('ShowDialog()')
action('SetDialog("King Heinrich: Now Now Witcher dont be mean, you had a feeling to be here thats why you are here")')
action('ShowDialog()')
action('SetDialog("Evander: Tell me what is that you want of me, if you are here just to make small talk and waste my time, I shall leave")')
action('ShowDialog()')
action('SetDialog("King Heinrich: Seems like you are the same old guy Witcher, anyways, I have a small task for you: There is a demon that haunts this kingdom, but its not a demon completely, its half human and half demon. Go and kill it")')
action('ShowDialog()')
action('SetDialog("Evander: You know I dont kill humans right")')
action('ShowDialog()')
action('SetDialog("King Heinrich: I know you dont I guess you dont have any other choice")')
action('ShowDialog()')
action('Wait(5s)')
action('HideDialog()')



action('SetExpression(Evander, Angry)')

while(True):
	input() 
