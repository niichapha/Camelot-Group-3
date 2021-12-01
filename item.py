from _typeshed import Self
from actioncomm import action

class Item:
    def __init__(self,varname,obj):
        self.varname=varname
        self.obj=obj
    
    varname=input()
    obj=input()

    def item_action(self):
        action('CreateItem('+self.varname+','+self.obj+')')


item=Item()
item.item_action()

