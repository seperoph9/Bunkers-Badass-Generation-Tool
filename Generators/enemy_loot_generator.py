import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file
import random



import random

def generate_enemy_loot():
	badass_rank = int(input("What is the badass rank for the enemy slain? "))
	print("Badass Rank : ",badass_rank)

	badass_chart = {
		(1,3): 1,
		(4,6): 2,
		(7,12): 3,
		(13,18): 4,
		(19,24): 5,
		(25,100): 6,
	}
	enemy_drop_table = {
		1: [
			{"item": "10g"},
			{"item": "30g"},
			{"item": "Health Potion (3d8+10)"},
			{"Potions":2},
			{"Grenade":1},
			{"Grenade":1},
		],
		2: [
			{"item": "Health Potion (1d8)"},
			{"item": "Health Potion (2d8+5)"},
			{"item": "Shield Potion (3d8+10)"},
			{"Grenade":1},
			{"Shield":1},
			{" Relic":2}
		],
		3: [
			{"item": "Shield Potion (1d8)"},
			{"item": "Shield Potion (1d8)"},
			{"item": "Random Potion (1)"},
			{"item": "Shield Mod"},
			{"item": "Common Relic"},
			{"Gun":0},
		],
		4: [
			{"Grenade":1},
			{"Grenade":3},
			{"Grenade":3},
			{"Gun":0},
			{"Gun":0},
			{"Gun":0},
		]
	}
	chest = []
	# Determine the loot tier based on badass rank
	loot_tier = None
	for range_, tier in badass_chart.items():
		if range_[0] <= badass_rank <= range_[1]:
			loot_tier = tier
			break

	if loot_tier is not None:
		# Roll for enemy loot
		enemy_roll = random.randint(1, 4)
		loot_line = enemy_drop_table[enemy_roll]

		# Determine how far to iterate based on the result of the badass chart
		iteration_limit = min(loot_tier, len(loot_line))

		# Generate loot items based on the loot line and iteration limit
		for i in range(iteration_limit):
			loot_item = loot_line[i]
			print(loot_item)

			# Iterate over each key-value pair in the loot item dictionary
			for key, value in loot_item.items():
				# Check the type of loot and handle it accordingly
				if key == 'item':
					chest.append(value)  # Add the item to the chest
				elif key == 'Potions':
					for _ in range(value):  # Add specified number of potions
						chest.append(generate_potion())
				elif key == 'Grenade':
					for _ in range(value):  # Add specified number of grenades
						chest.append(generate_grenade())
				elif key == 'Shield':
					for _ in range(value):  # Add specified number of shields
						chest.append(generate_shield())
				elif key == 'Relic':
					for _ in range(value):  # Add specified number of relics
						chest.append(generate_relic())
				elif key == 'Gun':
					for _ in range(value):  # Add specified number of guns
						chest.append(generate_gun())
						
		chest = '\n'.join(chest)
		filename = 'Generated_Items.txt'
		with open(filename, 'w') as file:
			file.write(chest)
		#save_to_file("Generated_Items.txt", '\n'.join(chest))
		return chest
	
