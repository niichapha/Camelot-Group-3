from typing import NamedTuple
from Narration import Narration
from actioncomm import action

class Narration_methods(Narration):
    def sub_dialoge():
        action('SetDialog()')
        action('ShowDialog()')
        action('Wait(3)')
        action('HideDialog()')



