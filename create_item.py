# need to pass argument- item_name, item-type, position 
# to create a item and palce that item in particular position

from action import action
class item:
    def __init__(self,item_name,item,position):
        self.item_name=item_name
        self.item=item
        self.position=position
        
    def create_item(item_name,item,position):
        action('CreateItem('+item_name+','+item+')')
        action('SetPosition('+item_name+','+position+')')