from action import action

def Message(Name, dialogue):
    action('SetNarration('+Name+': '+dialogue+')')
    action('ShowNarration')
    action('Wait(3)')
    action('HideNarration')