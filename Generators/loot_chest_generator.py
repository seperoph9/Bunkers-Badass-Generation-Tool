import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file
def generate_loot_chest():
	chest_loot_table = {
		1:{'contents':"MIMIC"},2:{'contents':"MIMIC"},3:{'contents':"MIMIC"},
		4:{'contents':"Common Health potion"},
		5:{'Gun':1},
		6:{'contents':"Common Gun Favored"},
		7:{'Grenade':2},
		8:{'Shield':1},
		9:{'Gun':2},
		10:{'contents':"Uncommon Gun Favored"},
		11:{'contents':"Uncommon Health potion"},
		12:{'contents':"Uncommon Shield Potion"},
		13:{'Gun':3},
		14:{'contents':"Rare Gun Favored"},
		15:{'Grenade':2,'Shield':1},
		16:{'Gun':4},
		17:{'contents':"Epic Gun Favored"},
		18:{'contents':"Epic Health Potion"},
		19:{'Relic':3},
		20:{'Gun':5},
		21:{'contents':"Legendary Gun Favored"}
	}

	chest = []

	total_rolls = random.randint(1,len(chest_loot_table))

	if chest_loot_table[total_rolls].get('contents'):
		chest.append(chest_loot_table[total_rolls].get('contents'))
		

	# Generating any needed loot
	#
	# Get Random Potions
	if chest_loot_table[total_rolls].get('Potion'):
		for i in range(chest_loot_table[total_rolls]['Potion']):
			chest.append(generate_potion())
	
	# Get Random Grenades
	if chest_loot_table[total_rolls].get('Grenade'):
		for j in range(chest_loot_table[total_rolls]['Grenade']):
			chest.append(generate_grenade())
	
	# Get Random Shield
	if chest_loot_table[total_rolls].get('Shield'):
		for k in range(chest_loot_table[total_rolls]['Shield']):
			chest.append(generate_shield())
	
	# Get Random Gun of Rarity
	if chest_loot_table[total_rolls].get('Gun'):
		chest.append(generate_gun(chest_loot_table[total_rolls]['Gun']))
	
	# Get Random Relics of Rarity[0] & Amount[1]
	if chest_loot_table[total_rolls].get('Relic'):
		for l in range(chest_loot_table[total_rolls]['Relic'][1]):
			chest.append(generate_relic(chest_loot_table[total_rolls]['Relic'][0]))


	#print('All rolls', die_rolls, '\nTotal:', total_rolls, '\nCache Loot:', chest)
	
	# Saving Items to file
	save_to_file("Generated_Items.txt", '\n'.join(chest))

	# Give back chest items
	return chest