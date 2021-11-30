from action import action
from create_item import create_item


def BlackSmith(Evander, owner):
    action('Enter('+Evander.name+',Blacksmith.Door)')
    create_item('Sword','Sword','Blacksmith.Table')
    action('WalkTo('+Evander.name+',Sword)')
    action('Take('+Evander.name+',Sword)')
    action('WalkTo('+Evander.name+', '+b_shop_vendor.name+')')
    action('Face('+b_shop_vendor.name+','+Evander.name+')')
    action('SetNarration('+Evander.name+': Hi! can I get this sword please)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('SetNarration('+b_shop_vendor.name+': Sure! Have a good day!)')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')
    action('Exit('+Evander.name+',Blacksmith.Door')