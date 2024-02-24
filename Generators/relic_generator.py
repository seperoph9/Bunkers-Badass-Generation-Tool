import random
# 
# Generate Relic
# 
def generate_relic(custom_rarity):
	custom_rarity = int(custom_rarity)
	classroll = random.randint(1,9)
	classes = {
		1:"Assasin's",
		2:"Berserker's",
		3:"Commando's",
		4:"Gunzerker's",
		5:"Hunter's",
		6:"Mecromancer's",
		7:"Psyco's",
		8:"Siren's",
		9:"Soldier's"
	 }
	chosen_class = classes[classroll]

	common_relics = {
		(1, 5): "Relic   -   (Vitality)   -   Rarity (Common)   -   Effect (+20 Health)   -   Class Effect (+5 health from potions)",
		(6, 10): "Relic   -   (Stockpile)   -   Rarity (Common)   -   Effect (+2 max grenades)   -   Class Effect (+1 grenade from lootpiles)",
		(11, 15): "Relic   -   (Protection)   -   Rarity (Common)   -   Effect (+15 Max shields)   -   Class Effect (+10 recharge rate)",
		(16, 20): "Relic   -   (Aggression)   -   Rarity (Common)   -   Effect (+3 Damage for favored gun)   -   Class Effect (+1 damage to all guns)",
		(21, 25): "Relic   -   (Resistance)   -   Rarity (Common)   -   Effect (+1d4 Elemental Resistance)   -   Class Effect (+1d4 Damage Resistance)",
		(26, 30): "Relic   -   (Tenacity)   -   Rarity (Common)   -   Effect (+1 Initiative Modifer)   -   Class Effect (+10 Health)",
		(31, 35): "Relic   -   (Elemental)   -   Rarity (Common)   -   Effect (+2 Elemental Damage)   -   Class Effect (+20 percent on Elemental Rolls)",
		(36, 40): "Relic   -   (Strength)   -   Rarity (Common)   -   Effect (+3 Melee Damage)   -   Class Effect (+1 melee Attack/turn)",
	}
	uncommon_relics = {
		(41, 45): "Relic   -   (Vitality)   -   Rarity (Uncommon)   -   Effect (+30 max Health)   -   Class Effect (+10 Health from Potions)",
		(46, 50): "Relic   -   (Stockpile)   -   Rarity (Uncommon)   -   Effect (+2 Grenades)   -   Class Effect (+2 grenades from loot piles)",
		(51, 55): "Relic   -   (Protection)   -   Rarity (Uncommon)   -   Effect (+20 Max Shields)   -   Class Effect (+15 Recharge Rate)",
		(56, 60): "Relic   -   (Aggression)   -   Rarity (Uncommon)   -   Effect (+4 Damage from favored guns)   -   Class Effect (+2 Damage to all guns)",
		(61, 65): "Relic   -   (Resistance)   -   Rarity (Uncommon)   -   Effect (+1d6 Elemental Resistance)   -   Class Effect (+1d6 Damage Resistance)",
		(66, 70): "Relic   -   (Tenacity)   -   Rarity (Uncommon)   -   Effect (+2 Initiative)   -   Class Effect (+15 Health)",
		(71, 75): "Relic   -   (Elemental)   -   Rarity (Uncommon)   -   Effect (+3 Elemental Damage)   -   Class Effect (+30 percent on elemental rolls)",
		(76, 80): "Relic   -   (Strength)   -   Rarity (Uncommon)   -   Effect (+4 Melee Damage)   -   Class Effect (+2 Melee Attacks/turn)",
	}
	rare_relics = {
		(81, 85): "Relic   -   (Vitality)   -   Rarity (Rare)   -   Effect (+40 Max Health)   -   Class Effect (+15 Health from potions)",
		(86, 90): "Relic   -   (Stockpile)   -   Rarity (Rare)   -   Effect (+4 Max Grenades)   -   Class Effect (+3 grenades from loot piles)",
		(91,95): "Relic   -   (Protection)   -   Rarity (Rare)   -   Effect (+25 max Shields)   -   Class Effect (+20 Recharge Rate)",
		(96,96): "Relic   -   (Agression)   -   Rarity (Rare)   -   Effect (+5 Damage for favored Gun)   -   Class Effect (+3 damage to all guns)",
		(97,97): "Relic   -   (Resistance)   -   Rarity (Rare)   -   Effect (+1d6 elemental resistance)   -   Class Effect (+1d8 damage resistance)",
		(98,98): "Relic   -   (Tenacity)   -   Rarity (Rare)   -   Effect (+3 Initiative Mod)   -   Class Effect (+20 Health)",
		(99,99): "Relic   -   (Elemental)   -   Rarity (Rare)   -   Effect (+4 Elemental Damage)   -   Class Effect (+40 Percent on elemental rolls)",
		(100,100): "Relic   -   (Strength)   -   Rarity (Rare)   -   Effect (+5 melee Damage)   -   Class Effect (+3 Melee Attacks/turn)",
	}
	relics = {
		(1, 5): "Relic   -   (Vitality)   -   Rarity (Common)   -   Effect (+20 Health)   -   Class Effect (+5 health from potions)",
		(6, 10): "Relic   -   (Stockpile)   -   Rarity (Common)   -   Effect (+2 max grenades)   -   Class Effect (+1 grenade from lootpiles)",
		(11, 15): "Relic   -   (Protection)   -   Rarity (Common)   -   Effect (+15 Max shields)   -   Class Effect (+10 recharge rate)",
		(16, 20): "Relic   -   (Aggression)   -   Rarity (Common)   -   Effect (+3 Damage for favored gun)   -   Class Effect (+1 damage to all guns)",
		(21, 25): "Relic   -   (Resistance)   -   Rarity (Common)   -   Effect (+1d4 Elemental Resistance)   -   Class Effect (+1d4 Damage Resistance)",
		(26, 30): "Relic   -   (Tenacity)   -   Rarity (Common)   -   Effect (+1 Initiative Modifer)   -   Class Effect (+10 Health)",
		(31, 35): "Relic   -   (Elemental)   -   Rarity (Common)   -   Effect (+2 Elemental Damage)   -   Class Effect (+20 percent on Elemental Rolls)",
		(36, 40): "Relic   -   (Strength)   -   Rarity (Common)   -   Effect (+3 Melee Damage)   -   Class Effect (+1 melee Attack/turn)",
		(41, 45): "Relic   -   (Vitality)   -   Rarity (Uncommon)   -   Effect (+30 max Health)   -   Class Effect (+10 Health from Potions)",
		(46, 50): "Relic   -   (Stockpile)   -   Rarity (Uncommon)   -   Effect (+2 Grenades)   -   Class Effect (+2 grenades from loot piles)",
		(51, 55): "Relic   -   (Protection)   -   Rarity (Uncommon)   -   Effect (+20 Max Shields)   -   Class Effect (+15 Recharge Rate)",
		(56, 60): "Relic   -   (Aggression)   -   Rarity (Uncommon)   -   Effect (+4 Damage from favored guns)   -   Class Effect (+2 Damage to all guns)",
		(61, 65): "Relic   -   (Resistance)   -   Rarity (Uncommon)   -   Effect (+1d6 Elemental Resistance)   -   Class Effect (+1d6 Damage Resistance)",
		(66, 70): "Relic   -   (Tenacity)   -   Rarity (Uncommon)   -   Effect (+2 Initiative)   -   Class Effect (+15 Health)",
		(71, 75): "Relic   -   (Elemental)   -   Rarity (Uncommon)   -   Effect (+3 Elemental Damage)   -   Class Effect (+30 percent on elemental rolls)",
		(76, 80): "Relic   -   (Strength)   -   Rarity (Uncommon)   -   Effect (+4 Melee Damage)   -   Class Effect (+2 Melee Attacks/turn)",
		(81, 85): "Relic   -   (Vitality)   -   Rarity (Rare)   -   Effect (+40 Max Health)   -   Class Effect (+15 Health from potions)",
		(86, 90): "Relic   -   (Stockpile)   -   Rarity (Rare)   -   Effect (+4 Max Grenades)   -   Class Effect (+3 grenades from loot piles)",
		(91,95): "Relic   -   (Protection)   -   Rarity (Rare)   -   Effect (+25 max Shields)   -   Class Effect (+20 Recharge Rate)",
		(96,96): "Relic   -   (Agression)   -   Rarity (Rare)   -   Effect (+5 Damage for favored Gun)   -   Class Effect (+3 damage to all guns)",
		(97,97): "Relic   -   (Resistance)   -   Rarity (Rare)   -   Effect (+1d6 elemental resistance)   -   Class Effect (+1d8 damage resistance)",
		(98,98): "Relic   -   (Tenacity)   -   Rarity (Rare)   -   Effect (+3 Initiative Mod)   -   Class Effect (+20 Health)",
		(99,99): "Relic   -   (Elemental)   -   Rarity (Rare)   -   Effect (+4 Elemental Damage)   -   Class Effect (+40 Percent on elemental rolls)",
		(100,100): "Relic   -   (Strength)   -   Rarity (Rare)   -   Effect (+5 melee Damage)   -   Class Effect (+3 Melee Attacks/turn)",
	}
	
	# if custom_rarity:
	# 	pass
	# else:
	# 	roll_result = random.randint(1,100)
	# 	for pick in relics.keys():
	# 		if roll_result in range(pick):
	# 			return chosen_class+" "+entry

	if custom_rarity == 0:
		roll_result = random.randint(1,100)
		for pick in relics.keys():
			if roll_result in range(pick[0], pick[1]+1):
				return chosen_class + " " + relics[pick]
	elif custom_rarity > 0:
		if custom_rarity == 1:
			roll_result = random.randint(1,40)
			for pick in common_relics.keys():
				if roll_result in range(pick[0], pick[1]+1):
					return chosen_class + " " + common_relics[pick]
		if custom_rarity == 2:
			roll_result = random.randint(41,80)
			for pick in uncommon_relics.keys():
				if roll_result in range(pick[0], pick[1]+1):
					return chosen_class + " " + uncommon_relics[pick]
		if custom_rarity == 3:
			roll_result = random.randint(81,100)
			for pick in rare_relics.keys():
				if roll_result in range(pick[0], pick[1]+1):
					return chosen_class + " " + rare_relics[pick]