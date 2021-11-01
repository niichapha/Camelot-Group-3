from action import action

def all_game_setup():
    action('SetTitle(\"The Destiny\")', False)
    action("SetCredits(\"Experience Manager by Vijay Varshini Lakshmi Narayanan, Narendra Nath, Nichapha Manoonwong , Varun Venkatesh, Akshay Reddy\")", False)
    
# Create Game Locations
    action('CreatePlace(BookPlace, Library)')
    action('CreatePlace(Castle, GreatHall)')
    action('CreatePlace(Alchemy, AlchemyShop)')
    action('CreatePlace(WeaponShop, Blacksmith)')
        

# Create Characters

    # Main Character(Witcher Evander)
    action('CreateCharacter(Evander, B)')
    action('SetEyeColor(Evander, Brown)', False)
    action('SetHairStyle(Evander, Spiky)', False)
    action('SetHairColor(Evander, Brown)', False)
    action('SetClothing(Evander, Noble)', False)

    # King Heinrich
    action('CreateCharacter(King Heinrich, H)')
    action('SetEyeColor(King Heinrich, Brown)', False)
    action('SetHairStyle(King Heinrich, Mage_Full)', False)
    action('SetHairColor(King Heinrich, Gray)', False)
    action('SetClothing(King Heinrich, King)', False)

    # Princess Aida
    action('CreateCharacter(Princess Aida, C)')
    action('SetEyeColor(Princess Aida, Blue)', False)
    action('SetHairStyle(Princess Aida, Short)', False)
    action('SetHairColor(Princess Aida, Brown)', False)
    action('SetClothing(Princess Aida, Noble)', False)
    
#creating Items
    	action('CreateItem("HealingPotion",BluePotion)')
	action('CreateItem("FirePotion", RedPotion)')
	action('CreatItem("EnergyPotion",PurplePotion)')
	action('CreateItem("Swords",Sword)')
	action('CreateItem("Hammers",Hammer)')
	
#SetPosition for Items
	 action('SetPosition(HealingPotion, Alchemy.AlchemistTable.Center)', False)
	 action('SetPosition(FirePotion, Alchemy.AlchemistTable.Right)', False)
 	 action('SetPosition(EnergyPotion, Alchemy.Table.FrontRight)', False)
	 action('SetPosition(Swords, WeaponShop.Chest)', False)
	 action('SetPosition(Hammers, WeaponShop.Table.Right)', False)	
    
#creating clues for alchemist_shop

action('CreateItem(Energy Potion, PurplePotion)', False)

#creating clues for blacksmith_shop
action('CreateItem(Sword of Heisenberg , Sword)', False)
