from action import action

def all_game_setup():
    action('SetTitle(\"The Destiny\")', False)
    action("SetCredits(\"Experience Manager by Vijay Varshini Lakshmi Narayanan, Narendra Nath, Nichapha Manoonwong , Varun Venkatesh, Akshay Reddy\")", False)
    
# Create Game Locations
    action('CreatePlace(BookPlace, Library)')
    action('CreatePlace(Castle, GreatHall)')
    action('CreatePlace(Alchemy, AlchemyShop)')
    action('CreatePlace(Weaponshop, Blacksmith)')
    
#creating clues for alchemist_shop

action('CreateItem(Energy Potion, PurplePotion)', False)

#creating clues for blacksmith_shop
action('CreateItem(Sword of Heisenberg , Sword)', False)
