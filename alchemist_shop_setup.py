from action import action 

def alchemist_shop_setup():
	
	action('StopSound()')
	action('PlaySound(Serenity, AlchemyShop, True)')
	action('Enter(Evander, AlchemyShop.Door, true)')
	action('SetCameraFocus(Evander)')
	action('SetCameraMode(follow)')
	#action('CreateItem(, BluePotion)')
	#action('CreateItem(Potion2, RedPotion)')
	#action('CreateItem(EnergyPotion, PurplePotion)')
	action('CreateItem("BluePotion",BluePotion)')
	action('CreateItem("RedPotion", Red)')
	action('CreatItem("PurplePotion",PurplePotion)')
	action('CreateItem("Sword",Sword)')
	action('CreateItem("Hammer",Hammer)')
	action('SetPosition(Potion1, AlchemyShop.AlchemistTable.Center)', False)
	action('SetPosition(Potion2, AlchemyShop.AlchemistTable.Right)', False)
	action('SetPosition(Potion3, AlchemyShop.Table.FrontLeft)', False)
	action('Pickup(Evander, BluePotion, AlchemyShop.AlchemistTable)')
	action('Pickup(Evander, RedPotion, AlchemyShop.AlchemistTable)')
	action('Pickup(Evander, PurplePotion, AlchemyShop.Table)')
	action('Exit(Evander, AlchemyShop.Door, true)')
	action('EnableInput()')
	
	#Enable effect in the environment 
	action('EnableEffect(QueensCastle.Fireplace, Campfire)', False)
	
	
