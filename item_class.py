from action import action
class item:

    def __init__(self,item_name,position):
        self.item_name=item_name
        self.position=position

    def item_creation(item_name,item,position):
        action('CreateItem('+item_name+','+item+')')
        action('SetPosition('+item_name+','+position+')')