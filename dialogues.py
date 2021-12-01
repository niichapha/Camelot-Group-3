from actioncomm import action

def dialogue_char(msg):
    action('SetDialog("'+msg+'")')
    action('ShowDialog()')