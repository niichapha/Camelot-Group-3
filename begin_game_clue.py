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

    #alchemyshop guy
    action('CreateCharacter(Jason, F)')
    action('SetClothing(Jason, Merchant)', False)
    action('SetHairStyle(Jason, Spiky)', False)
    action('SetPosition(Jason, Alchemy.Bar)')
    action('MoveAway(Alchemy.Bar)')
    action('WalkToSpot(Jason, 925.3, 0.3, 5.0)', False)
    action('SetExpression(Jason, happy)', False)
    action('SetSkinColor(Jason, 7)', False)
	
    #Blacksmith guy
    action('CreateCharacter(Aoki, F)')
    action('SetClothing(Aoki, Merchant)', False)
    action('SetHairStyle(Aoki, Spiky)', False)
    action('SetPosition(Aoki, WeaponShop.Table)')
    action('SetExpression(Aoki, happy)', False)
    action('SetSkinColor(Aoki, 5)', False)
	
#SetPosition for Items
	 action('SetPosition(HealingPotion, Alchemy.AlchemistTable.Center)', False)
	 action('SetPosition(FirePotion, Alchemy.AlchemistTable.Right)', False)
 	 action('SetPosition(EnergyPotion, Alchemy.Table.FrontRight)', False)
	 action('SetPosition(SwordofHeisenberg, WeaponShop.Chest)', False)
	 action('SetPosition(HammerofHeisenberg, WeaponShop.Table.Right)', False)	
    
#creating clues for alchemist_shop

action('CreateItem(EnergyPotion, PurplePotion)', False)
action('CreateItem("HealingPotion",BluePotion)',False)
action('CreateItem("FirePotion", RedPotion)',False)


#creating clues for blacksmith_shop
action('CreateItem(SwordofHeisenberg , Sword)', False)
action('CreateItem(HammerofHeisenberg , Hammer)', False)
