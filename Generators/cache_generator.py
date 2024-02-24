import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file
def generate_cache(dice: int):
	chest = []
	# 1. Single/Tiny Chest: 1d6
	# 2. Small Cache: 2d6
	# 3. Medium Cache: 3d6
	# 4. Medium Chest: 4d6
	# 5. Large Cache: 5d6
	# 6. Legendary Cache 6d6
	
	die_rolls = [random.randint(1,6) for i in range(dice)]

	total_rolls = sum(die_rolls)
	
	cachedict = {
		1:{'contents':["30g"]},
		2:{'contents':["Common Health Potion   -   Effect(1d8 Health)"]},
		3:{'contents':["Common Shield Potion   -   Effect(1d8 Shield)"]},
		4:{'contents':["30g + Common Health Potion   -   Effect(1d8 Health) Effect(1d8 Health)"]},
		5:{'contents':["30g + Common Shield Potion   -   Effect(1d8 Shield)"]},
		6:{'contents':["30g"], 'Potion':1},
		7:{'contents':["30g", "Uncommon Health Potion   -   Effect(1d8+5 Health)"]},
		8:{'contents':["30g", "Uncommon Shield Potion   -   Effect(1d8+5 Shield)"]},
		9:{'contents':["50g", "Uncommon Health Potion   -   Effect(1d8+5 Health)"]},
		10:{'contents':["50g", "Uncommon Shield Potion   -   Effect(1d8+5 Shield)"]},
		11:{'contents':["50g"], 'Gun':1}, # Common Gun
		12:{'contents':["80g", "Common Health Potion   -   Effect(1d8 Health)"]},
		13:{'contents':["80g", "Uncommon Health Potion   -   Effect(1d8+5 Health)"], 'Potion':1},
		14:{'contents':["80g", "Uncommon Shield Potion   -   Effect(1d8+5 Shield)"], 'Grenade':2},
		15:{'contents':["80g"], 'Potion':2, 'Relic':[1,1]}, # Common Relic
		16:{'contents':["80g"], 'Gun':2, 'Grenade':2}, # Uncommon Gun
		17:{'contents':["80g", "Uncommon Health Potion   -   Effect(1d8+5 Health)"], 'Gun':2}, # Uncommon Gun
		18:{'contents':["100g"], 'Grenade':2, 'Potion':2},
		19:{'contents':["100g"], 'Gun':2, 'Potion':1}, # Uncommon Gun
		20:{'contents':["100g", "Rare Health Potion(2)   -   Effect(2d8+5 Health)"], 'Grenade':1},
		21:{'contents':["100g", "Rare Shield Potion(2)   -   Effect(2d8+5 Shield)"], 'Grenade':1},
		22:{'contents':["100g"], 'Potion':3, 'Relic':[2,1]}, # Uncommon Relic
		23:{'contents':["100g"], 'Gun':3, 'Shield':1}, # Rare Gun
		24:{'contents':["100g"], 'Gun':3, 'Grenade':2, 'Shield':1}, # Rare Gun
		25:{'contents':["120g", "Rare Health Potion(2)   -   Effect(2d8+5 Health)"], 'Relic':[1,2], 'Grenade':2}, # Common Relic
		26:{'contents':["120g"], 'Grenade':3, 'Potion':2},
		27:{'contents':["120g"], 'Gun':3, 'Potion':2}, # Rare Gun
		28:{'contents':["120g", "Twofer Potion(2)"], 'Relic':[2,1], 'Shield':1}, # Uncommon Relic
		29:{'contents':["120g"], 'Gun':3, 'Grenade':1}, # Rare Gun
		30:{'contents':["150g", "Epic Health Potion(2)   -   Effect(3d8+10 Health)", "Epic Shield Potion"], 'Grenade':1}, 
		31:{'contents':["150g"], 'Relic':[3, 2], 'Shield':1, 'Potion':2}, # Rare Relic x2
		32:{'contents':["150g"],"Gun":4, 'Potion':2, 'Grenade':1}, # Epic Gun
		33:{'contents':["150g"],"Gun":4, 'Grenade':6}, # Epic Gun
		34:{'contents':["150g"], 'Potions':3, 'Grenade':1, 'Relic':[3,1]}, # Rare Relic
		35:{'contents':["150g", "Epic Health Potion(3)   -   Effect(3d8+10 Health)"], 'Gun':4, 'Relic':[3,1], 'Shield':1}, # Epic Gun + Rare Relic
		36:{'contents':["200g", "Epic Health Potion(3)   -   Effect(3d8+10 Health)"], 'Gun':4, 'Grenade':6, 'Shield':1, 'Relic':[3,2]}, # Epic Gun + Rare Relic x2
	}

	chest = cachedict[total_rolls]['contents'].copy()

	# Generating any needed loot
	#
	# Get Random Potions
	if cachedict[total_rolls].get('Potion'):
		for i in range(cachedict[total_rolls]['Potion']):
			chest.append(generate_potion())
	
	# Get Random Grenades
	if cachedict[total_rolls].get('Grenade'):
		for j in range(cachedict[total_rolls]['Grenade']):
			chest.append(generate_grenade())
	
	# Get Random Shield
	if cachedict[total_rolls].get('Shield'):
		for k in range(cachedict[total_rolls]['Shield']):
			chest.append(generate_shield())
	
	# Get Random Gun of Rarity
	if cachedict[total_rolls].get('Gun'):
		chest.append(generate_gun(cachedict[total_rolls]['Gun']))
	
	# Get Random Relics of Rarity[0] & Amount[1]
	if cachedict[total_rolls].get('Relic'):
		for l in range(cachedict[total_rolls]['Relic'][1]):
			chest.append(generate_relic(cachedict[total_rolls]['Relic'][0]))


	#print('All rolls', die_rolls, '\nTotal:', total_rolls, '\nCache Loot:', chest)
	
	# Saving Items to file
	save_to_file("Generated_Items.txt", '\n'.join(chest))

	# Give back chest items
	return chest