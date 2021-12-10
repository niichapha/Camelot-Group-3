from attack import attack
from item import create_item
from Narration import Message


def check_for_success(command):
    # keep getitng responses until the success of fail the given command is received
    while True:
        received = input()
        
        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False

        
def action(command):
    print('start ' + command)
    #call function to check for its success
    return check_for_success(command)

def options():
    while True:
        received = input()
        if received == 'input Exit City.EastEnd':

			def Port_Setup():
				attack('Evander, Soldier1')
				action('SetPosition(Yenefer, Port.BigShip)')
				action('EnableInput()')
				Narration.Message(''+Evander.name+'', 'Are you Yenefer from Wilderguard?'+Yenefer.name+'')
				Narration.Message(''+Yenefer.name+'', 'Oh look who it is, the Famous Withcer, Evander!'+Evander.name+'')
				action('SetExpression(Evander, Laugh)')
				Narration.Message(''+Evander.name+'', 'So you do remember me!'+Yenefer.name+'')
				Narration.Message(''+Yenefer.name+'', 'Of course I would after the brief meeting we had a while back'+Evander.name+'')
				action('SetExpressiong(Evander, neutral)')
				Narration.Message(''+Evander.name+'', 'I felt bad leaving you unsaid, and I really miss you'+Yenefer.name+'')
				Narration.Message(''+Yenefer.name+'', 'We should probably hangout sometime'+Evander.name+'')
				Narration.Message(''+Evander.name+'', 'I was going towards the Tavern, if you are free you can join me!'+Yenefer.name+'')
				Narration.Message(''+Yenefer.name+'', 'Sure, I just landed here you can show me around!'+Evander.name+'')
				action('Exit(Yenefer, Port.Exit, true)')
				action('Exit(Evander, Port.Exit, true)')

			def Tavern_setup():
				action('Enter(Evander, Tavern.Door, true)')
				action('Enter(Yenefer, Tavern.Door, true)')
				item.create_item('BeerMug', 'Mug', 'Tavern.Bar.Left)')
				item.create_item('BeerMug', 'Mug', 'Tavern.Bar.Right)')
				action('EnableInput()')
				action('WalkTo(Yenefer, Tavern.Bar)')
				action('Wait(5s)')
				action('Drink(Evander)')
				action('Drink(Yenefer)')
				Narration.Message(''+Evander.name+'', 'So what have you been upto?'+Yenefer.name+'')
				Narration.Message(''+Yenefer.name+'', 'I am a Witch for Mulduar'+Yenefer.name+'')
				Narration.Message(''+Evander.name+'', 'Oh that Nasty place.'+Yenefer.name+'')
				Narration.Message(''+Evander.name+'', 'How have you been managing there?'+ Yenefer.name+'')
				action('Drink(Evander)')
				action('Drink(Yenefer)')
				Narration.Message(''+Yenefer.name+'', 'I get Free beer!'+Evander.name+'')
				action('SetExpression(Evander, Laugh)')
				action('SetExpression(Yenefer, Laugh)')
				action('SetExpression(Evander, Neutral)')
				action('SetExpression(Yenefer, Neutral)')
				Narration.Message(''+Evander.name+'', 'Do you want to join me on one small adventure?'+Yenefer.name+'')
				action('SetExpression(Yenefer, surprised)')
				Narration.Message(''+Yenefer.name+'', 'Oh now the Witcher wants me to spend more time with him'+Evander.name+'')
				action('SetExpression(Evander, happy)')
				Narration.Message(''+Evander.name+'', 'I know that you want to join me'+Yenefer.name+'')
				Narration.Message(''+Yenefer.name+'', 'Okay alright, I will come along.'+Evander.name+'')
				action('WalkTo(Yenefer, Tavern.Door)')
				action('Wait(5s)')
				action('Exit(Yenefer, Tavern.Door, true)')
				action('Exit(Evander, Tavern.Door, true)')

        elif received == 'input Exit City.WestEnd':
			action('SetPosition(Yenefer, Azkaban.Bed)')
			action('Sit(Soldier2, Azkaban.Chair)')
                        action('Enter(Evander, Azkaban.Door, true)')
			action('WalkTo(Soldier2, Evander)')
			attack(Evander, Soldier2)
			action('EnableInput()')
			action('Enter(Evander, Azkaban.CellDoor)')  #Doubt at this point
			action('SetPosition(Yenefer, Azkaban.Bed)')
			Narration.Message(''+Evander.name+'', 'Yenefer, are you okay??'+Yenefer.name+'')
			Narration.Message(''+Yenefer.name+'', 'The Witcher is here! Finally I Feel safe'+Evander.name+'')
			Narration.Message(''+Evander.name+'', 'How did you get into this mess?'+Yenefer.name+'')
			Narration.Message(''+Yenefer.name+'', 'There is a witch that is trying to kill me, because the kingdom I am in defeated hers.'+Evander.name+'')
			Narration.Message(''+Evander.name+'', 'Okay lets get you out of here before they figure out. Tell me the story on the way.'+Evander.name+'')
			action('Exit(Yenefer, Azkaban.door, true)')
			action('Exit(Evander, Azkaban.door, true)')


        action('SetNight()')
        action('Enter(Evander, Camp.Exit)')
        action('Enter(Yenefer, Camp.Exit)')
        action('EnableEffect(Camp.Firepit, Campfire)')
        action('Enter(Witch, Camp.Exit)')
        action('WalkTo(Witch, Yenefer)')
        action('Face(Witch, Yenefer)')
        Narration.Message(''+Yenefer.name+'', 'Ursula, It can not be you!!'+Yenefer.name+'')
        action('SetExpression(Yenefer, Surprised)')
        Narration.Message(''+Yenefer.name+'', 'How did you follow me here?'+Witch.name+'')
        Narration.essage(''+Witch.name+'', 'You do know that i am a witch too right?'+Yenefer.name+'')
        Narration.Message(''+Yenefer.name+'', 'Evander Please help me. This is the Witch that kidnapped me'+Evander.name+'')
        action('Attack(Evander, Witch, false)')
        action('Cast(Witch, Evander, blue)')
        action('Kneel(Evander)')
        action('Cast(Witch, Yenefer, green)')
        action('Die(Yenefer)')
        Narration.Message(''+Evander.name+'', 'How dare you kill her!!!'+Witch.name+'')
        Narration.Message(''+Witch.name+'', 'She deserves to die, and you are going to die next witcher!'+Evander.name+'')
        action('Cast(Evander, Witch, purple)')
        action('Die(Witch)')
        action('Revive(Yenefer)')
        action('Dance(Evander, Yenefer)')
