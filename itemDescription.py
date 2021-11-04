def inspect_item(item):
	action('DisableInput()')
	action('WalkTo(Evander, ' + item + ')')
	action('Face(Evander, ' + item + ')')
	action('EnableInput()')

	#Potions
	if item == 'BluePotion':
		#BluePotion is HealingPotion
		midscene_narration('The label reads - HealingPotion')
		action('PlaySound(Unlock, BluePotion, false)')
	
	elif item == 'PurplePotion':
		#PurplePotion is EnergyPotion
		midscene_narration('The label reads - EnergyPotion')
		action('PlaySound(Unlock, PurplePotion, false)')
		
	
	elif item == 'RedPotion':
		#RedPotion is FirePotion
		midscene_narration('The label reads - FirePotion')
		action('PlaySound(Unlock, RedPotion, false)')


	#Sword
	elif item == 'Sword':
		midscene_narration('The label reads - SwordofHeisenberg')
		action('PlaySound(Draw, Sword, false)')

	#Hammer
	elif item == 'Hammer':
		midscene_narration('The label reads - HammerofHeisenberg')
		action('PlaySound(Hammer, Hammer, false)')
