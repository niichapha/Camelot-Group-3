from _typeshed import Self
from actioncomm import action

class Enable:
    def __init__(self,stri,obje,person):
        self.str=stri
        self.obje=obje
        self.person=person
    
    stri=input()
    obje=input()
    person=input()

    def enable_action(self):
        action('EnableInput('+self.stri+','+self.obje+','+self.person+')')

enableobj=Enable()
enableobj.enable_action()





    


