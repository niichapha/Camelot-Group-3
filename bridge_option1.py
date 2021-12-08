from Narration import Narration
from action import action
from bridge import bridge
from attack import attack

class bridgeoption1(bridge):
    def bridge_scene1(Evander,princessaida,bridge_path,king,kingbodyguard):
        action('SetCameraFocus('+Evander.name+')')
        action('SetCameraMode(follow)')
        Narration.Message('Evander',':Do you want to dance with me your highness?')
        Narration.Message('Princess Aida',': Oh, I would love to do that')
        action('DanceTogether('+Evander.name+', '+princessaida.name+')')
        action('PlaySound(River, Bridge, true)')
        action('PlaySound(LivelyMusic, Bridge, true)')
        action('Wait(2)')
        action('StopSound(LivelyMusic, Bridge, true)')
        action('PlaySound(Danger1, Bridge, true)')
        action('Enter('+king.name+', '+bridge_path.name+'.NorthEnd)')
        action('Enter('+kingbodyguard.name+', '+bridge_path.name+'.NorthEnd)')
        action('SetExpression('+king.name+', angry)')
        action('StopSound(Danger1, Bridge, true)')
        Narration.Message('King Heinrich',':What are you doing with her?')
        action('SetExpression('+king.name+', Surprised)')
        Narration.Message('Evander',': Oh your Majesty!')
        Narration.Message('King Heinrich',': Kill her Now!!!')
        Narration.Message('Evander',': No, your Majesty!')
        attack()





    

