from item_class import item
from action import action

def item_creation(item_name,item,position):
    action('CreateItem('+item_name+','+item+')')
    action('SetPosition('+item_name+','+position+')')

item_obj=item()
item_obj.item_creation()