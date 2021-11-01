from action import action 

def alchemist_shop_setup():
	
	action('StopSound()')
	action('PlaySound(Serenity, Alch, True)')
	
	action('Enter(Evander, AlchemyShop.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	action('Pickup(Evander, BluePotion, AlchemyShop.AlchemistTable)')
	action('Pickup(Evander, RedPotion, AlchemyShop.AlchemistTable)')
	action('Pickup(Evander, PurplePotion, AlchemyShop.AlchemistTable)')
	action('Exit(Evander, AlchemyShop.Door, true)')
	action('EnableInput()')
