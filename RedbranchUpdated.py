from action import action
from create_item import item
from attack import attack
from Narration import Narration
from create_character import Create_character
from create_location import Create_location


Evander=Create_character('Evander','D','Merchant', 'Spiky')
Yenefer=Create_character('Yenfer', 'E', 'Witch', 'Ponytail')
Soldier2 = Create_character('Soldier2', 'D', 'HeavyArmour', 'Spiky')
Witch = Create_character('Witch', 'B', 'Witch', 'Ponytail')
Port = Create_location('Port', 'Port')
camp = Create_location('Camp', 'Camp')
Azkaban = Create_location('Azkaban', 'Dungeon')
city_location=Create_location('city', 'City')


def check_for_door():
    while True:
        received = input()
        if received == 'input east_exit city.EastExit':
            action('Enter(Yenefer,  Port.Exit)')
            action('SetPosition(Yenefer, Port.BigShip)')
            action('WalkTo(Evander, Yenefer)')
            Narration.Message('Evander', 'Are you Yenefer from Wilderguard?'+Yenefer.name+'')
            Narration.Message('Yenefer', 'Oh look who it is, the Famous Withcer, Evander!'+Evander.name+'')
            action('SetExpression(Evander, Laugh)')
            Narration.Message('Evander', 'So you do remember me!'+Yenefer.name+'')
            Narration.Message('Yenefer', 'Of course I would after the brief meeting we had a while back'+Evander.name+'')
            action('SetExpressiong(Evander, neutral)')
            Narration.Message('Evander', 'I felt bad leaving you unsaid, and I really miss you'+Yenefer.name+'')
            Narration.Message('Yenefer', 'We should probably hangout sometime'+Evander.name+'')
            Narration.Message('Evander', 'I was going towards the Tavern, if you are free you can join me!'+Yenefer.name+'')
            Narration.Message('Yenefer', 'Sure, I just landed here you can show me around!'+Evander.name+'')
            action('Exit(Yenefer, Port.Exit, true)')
            action('Exit(Evander, Port.Exit, true)')
            Camp()
        
        elif received == 'input west_exit city.WestExit':
            action('SetPosition(Yenefer, Azkaban.Bed)')
            action('Sit(Soldier2, Azkaban.Chair)')
            action('Enter(Evander, Azkaban.Door, true)')
            action('WalkTo(Soldier2, Evander)')
            attack(Evander, Soldier2)
            action('EnableInput()')
            action('Enter(Evander, Azkaban.CellDoor)')
            action('SetPositon(Yenefer, Azkaban.Bed)')
            Narration.Message('Evander.name', 'Yenefer, are you okay??'+Yenefer.name+'')
            Narration.Message('Yenefer', 'The Witcher is here! Finally I Feel safe'+Evander.name+'')
            Narration.Message('Evander.name', 'How did you get into this mess?'+Yenefer.name+'')
            Narration.Message('Yenefer', 'There is a witch that is trying to kill me, because the kingdom I am in defeated hers.'+Evander.name+'')
            Narration.Message('Evander', 'Okay lets get you out of here before they figure out. Tell me the story on the way.'+Evander.name+'')
            action('Exit(Yenefer, Azkaban.door, true)')
            action('Exit(Evander, Azkaban.door, true)')

def Camp():
    action('SetNight()')
    action('Enter(Evander, Camp.Exit)')
    action('Enter(Yenefer, Camp.Exit)')
    action('EnableEffect(Camp.Firepit, Campfire)')
    action('Enter(Witch, Camp.Exit)')
    action('WalkTo(Witch, Yenefer)')
    action('Face(Witch, Yenefer)')
    Narration.Message('Yenefer', 'Ursula, It can not be you!! Yenefer')
    action('SetExpression(Yenefer, Surprised)')
    Narration.Message('Yenefer.name', 'How did you follow me here? Witch')
    Narration.Message('Witch', 'You do know that i am a witch too right? Yenefer')
    Narration.Message('Yenefer', 'Evander Please help me. This is the Witch that kidnapped me Evander')
    action('Attack(Evander, Witch, false)')
    action('Cast(Witch, Evander, blue)')
    action('Kneel(Evander)')
    action('Cast(Witch, Yenefer, green)')
    action('Die(Yenefer)')
    Narration.Message('Evander', 'How dare you kill her!!! Witch')
    Narration.Message('Witch', 'She deserves to die, and you are going to die next witcher! Evander')
    action('Cast(Evander, Witch, purple)')
    action('Die(Witch)')
    action('Revive(Yenefer)')
    action('Dance(Evander, Yenefer)')


def city_loc():
    action('Enter(Evander, city_location.NorthEnd)')
    action('SetCameraFocus(Evander)')
    action('SetCameraMode(follow)')
    action('EnableIcon(west_exit, exit, city_location.EastEnd, "west_exit")')
    action('EnableIcon(east_exit, exit, city_location.WestEnd, "East_exit")')
    action('EnableInput()')
    check_for_door()


