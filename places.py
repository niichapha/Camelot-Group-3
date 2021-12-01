from actioncomm import action

class Places_game:
    def __init__(self,place_name,place):
        self.name=place_name
        self.place=place
        action('CreatePlace('+place_name+','+place+')')