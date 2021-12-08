from action import action

class bridge:
    def bridge_scene(Evander,princessaida,bridge_path):
        action('Enter('+Evander.name+', '+bridge_path.name+'.SouthEnd)')
        action('Enter('+princessaida.name+', '+bridge_path.name+'.WestEnd)')
        action('SetCameraFocus('+Evander.name+')')
        action('SetCameraMode(follow)')
        action('EnableInput()')
        action('SetExpression('+Evander.name+', happy)')
        action('SetExpression('+princessaida.name+', happy)')
        action('WalkTo('+Evander.name+','+bridge_path.name+'.WestEnd)')


    
    






