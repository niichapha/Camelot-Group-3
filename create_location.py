from action import action

class Create_location:   #Using A class to create Location
    
   def __init__(self,place_name,place):
        self.name=place_name
        self.place=place
        action('CreatePlace('+place_name+','+place+')')