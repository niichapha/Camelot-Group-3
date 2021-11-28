'''
Initial by Nichapha
Update 11/28/21
'''
from action import action

# Create Characters
    # Player(Witcher Evander)
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

     # Yennefer
    action('CreateCharacter(Yennefer, A)')
    action('SetHairStyle(Yennefer, Long)', False)
    action('SetHairColor(Yennefer, Brown)', False)
    action('SetClothing(Yennefer, Peasant)', False)

    # Merchant at Blacksmith & AlchemyShop
    action('CreateCharacter(Merchant, F)')
    action('SetClothing(Merchant, Merchant)', False)
    
    # Bandit
    action('CreateCharacter(Enemy, D)')
    action('SetClothing(Enemy, Bandit)', False)

    # Soldier
    action('CreateCharacter(Soldier, D)')
    action('SetClothing(Soldier, HeavyArmour)', False)

    # Stranger
    action('CreateCharacter(Stranger, G)')
    action('SetHairStyle(Stranger, Straight)', False)
    action('SetClothing(Stranger, Beggar)', False)

    # Spy
    action('CreateCharacter(Spy, D)')
    action('SetHairStyle(Stranger, Short)', False)
    action('SetClothing(Spy, LightArmour)', False)
