import random
from grenade_generator import generate_grenade
from relic_generator import generate_relic
from potion_generator import generate_potion
from gun_generator import generate_gun
from shield_generator import generate_shield
from save_generator import save_to_file


def generate_dice_chest_loot():

	dice_chest_loot_table = {
		1:{'Gun':1},
		2:{'contents':["Uncommon Gun Favored"]},
		3:{'contents':["Uncommon Gun Favored", 'Rare Health Potion']},
		4:{'contents':["Uncommon gun Favored"],'Relic':1},
		5:{'contents':["Uncommon Gun Favored"],'Potion':2},
		6:{'Gun':3},
		7:{'contents':["Rare Gun Favored"]},
		8:{'contents':["Rare Gun Favored"],'Grenade':2},
		9:{'contents':["Rare Gun Favored"],'Relic':2},
		10:{'contents':["Rare Gun Favored"],'Grenade':2,'Shield':1},
		11:{'Gun':4},
		12:{'contents':["Epic Gun Favored"]},
		13:{'contents':["Epic Gun Favored", "Epic Health Potion"]},
		14:{'contents':["Epic Gun Favored"],'Relic':3},
		15:{'contents':["Epic Gun Favored"],'Grenade':3,'Shield':1},
		16:{'Gun':5},
		17:{'contents':["Legendary Gun Favored"]},
		18:{'contents':["Legendary Gun Favored"],'Grenade':1},
		19:{'contents':["Legendary Gun Favored"],'Relic':4},
		20:{'contents':["Legendary Gun Favored"],'Shield':1,'Potion':3},
	}

	total_rolls = random.randint(1,len(dice_chest_loot_table))

	chest = []

	if dice_chest_loot_table[total_rolls].get('contents'):
		chest = dice_chest_loot_table[total_rolls].get('contents').copy()

	# Generating any needed loot
	#
	# Get Random Potions
	if dice_chest_loot_table[total_rolls].get('Potion'):
		for i in range(dice_chest_loot_table[total_rolls]['Potion']):
			chest.append(generate_potion())
	
	# Get Random Grenades
	if dice_chest_loot_table[total_rolls].get('Grenade'):
		for j in range(dice_chest_loot_table[total_rolls]['Grenade']):
			chest.append(generate_grenade())
	
	# Get Random Shield
	if dice_chest_loot_table[total_rolls].get('Shield'):
		for k in range(dice_chest_loot_table[total_rolls]['Shield']):
			chest.append(generate_shield())
	
	# Get Random Gun of Rarity
	if dice_chest_loot_table[total_rolls].get('Gun'):
		chest.append(generate_gun(dice_chest_loot_table[total_rolls]['Gun']))
	
	# Get Random Relics of Rarity[0] & Amount[1]
	if dice_chest_loot_table[total_rolls].get('Relic'):
		chest.append(generate_relic(dice_chest_loot_table[total_rolls]['Relic']))

	#print('All rolls', die_rolls, '\nTotal:', total_rolls, '\nCache Loot:', chest)
	
	# Saving Items to file
	save_to_file("Generated_Items.txt", '\n'.join(chest))

	# Give back chest items
	return chest