import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file
import random



import random

def generate_bounty_board():
	# Dictionary of quest types (Obvious)
	quest_types = {
		1: "Rescue Mission",
		2: "Bounty Hunt",
		3: "Artifact Retrieval",
		4: "Sabotage Operation",
		5: "Escort Mission",
		6: "Assassination Contract",
		7: "Survival Challenge",
		8: "Exploration Expedition",
		9: "Data Recovery",
		10: "Defend the Fortification",
		11: "Reconnaissance Task",
		12: "Stealth Infiltration",
		# 13: "Interstellar Diplomacy",
		14: "Hunting Grounds",
		15: "Relic Investigation",
		16: "Emergency Evacuation",
		17: "Hazardous Material Cleanup",
		18: "Extermination Campaign",
		19: "Ancient Relic Translation",
		20: "Technology Salvage",
		21: "Undercover Operation",
		22: "Raid on Enemy Base",
		23: "Rogue AI Elimination",
		24: "Prisoner Extraction",
		25: "Ritual Disruption",
		26: "Cursed Artifact Retrieval",
		27: "Invasion Defense",
		28: "Tactical Retreat",
		29: "Criminal Syndicate Takedown",
		30: "Wildlife Conservation",
		31: "Underground Resistance Support",
		32: "Artifact Smuggling Interception",
		33: "Virus Containment",
		34: "Underworld Negotiation",
		35: "Rogue Scientist Apprehension",
		36: "Supply Run",
		37: "Lost Colony Investigation",
		38: "Piracy Suppression",
		39: "Resource Extraction",
		40: "Botanical Research",
		41: "Mercenary Contract",
		42: "Arms Dealer Bust",
		43: "Alien Artifact Analysis",
		44: "Celestial Phenomenon Observation",
		45: "Wasteland Patrol",
		46: "Infiltrate Corporate Headquarters",
		47: "Rogue Planet Exploration",
		48: "Rescue Stranded Travelers",
		49: "Prevent Hostile Takeover",
		50: "Dungeon Delve"
	}

	# Dictionary of locations (Obvious)
	locations = {
		1: "Abandoned Mine",
		2: "Desert Oasis",
		3: "Haunted Forest",
		4: "Urban Ruins",
		5: "Volcanic Wasteland",
		6: "Frozen Tundra",
		7: "Space Station",
		8: "Underground Bunker",
		9: "Jungle Temple",
		10: "Alien Mothership",
		11: "Mystic Swamp",
		12: "Floating City",
		13: "Crystal Caves",
		14: "Hidden Valley",
		15: "Subterranean City",
		16: "Dimensional Rift",
		17: "Lost Civilization Ruins",
		18: "Sunken Ship",
		19: "Radioactive Wasteland",
		20: "Sky Fortress",
		21: "Ancient Observatory",
		22: "Asteroid Belt",
		23: "Underwater City",
		24: "Forbidden Temple",
		25: "Toxic Jungle",
		26: "Iceberg Citadel",
		27: "Underworld Nexus",
		28: "Stormy Seas",
		29: "Ghost Town",
		30: "Crashed Spaceship",
		31: "Dark Matter Nebula",
		32: "Underground Labyrinth",
		33: "Floating Islands	",
		34: "Urban Sprawl	",
		35: "Celestial Battlefield	",
		36: "Skyrim Peaks",
		37: "Abyssal Depths",
		38: "Interstellar Trade Hub",
		39: "Forgotten Fortress",
		40: "Techno-City",
		41: "Lost World",
		42: "Hidden Monastery",
		43: "Infested Hive",
		44: "Alien Research Facility",
		45: "Crystal Mountain",
		46: "Haunted Mansion",
		47: "Thundering Plains",
		48: "Solar Flare Canyon",
		49: "Toxic Waste Dump",
		50: "Savage Highlands"
	}

	# Dictionary of enemies ( List of all possible enemies)
	enemies = {
		1: "Cultist",
		2: "Bandit",
		3: "Martyr",
		4: "Badass Cultist",
		5: "Badass Bandit",
		6: "Badass Martyr",
		7: "Baby Dragon",
		8: "Blue Dragon",
		9: "Red Dragon",
		10: "Green Dragon",
		11: "Yellow Dragon",
		12: "Badass Baby Dragon",
		13: "Badass Blue Dragon",
		14: "Badass Red Dragon",
		15: "Badass Green Dragon",
		16: "Badass Yellow Dragon",
		17: "Dwarf",
		18: "Dwarf Miner",
		19: "Dwarfzerker",
		20: "Badass Dwarf",
		21: "Badass Dwarf Miner",
		22: "Badass Dwarfzerker",
		23: "Goblin",
		24: "Potion Master",
		25: "Goblin Cannoneer",
		26: "Bomb Boi",
		27: "Goblin Engineer",
		28: "Badass Goblin",
		29: "Badass Alchemist",
		30: "Badass Cannoneer",
		31: "Badass Bomber",
		32: "Badass Engineer",
		33: "Rock Golem",
		34: "Iron Golem",
		35: "Badass Rock Golem",
		36: "Badass Iron Golem",
		37: "Knight",
		38: "Archer",
		39: "Paladin",
		40: "Squire",
		41: "Death Knight",
		42: "Badass Knight",
		43: "Badass Archer",
		44: "Badass Paladin",
		45: "Badass Squire",
		46: "Badass Death Knight",
		47: "Mimic",
		48: "Badass Mimic",
		49: "Orc Basher",
		50: "Orc Warrior",
		51: "Orc Bushwhacker",
		52: "Orc Warlord",
		53: "Badass Orc Basher",
		54: "Badass Orc Warrior",
		55: "Badass Bushwhacker",
		56: "Badass Orc Warlord",
		57: "Pixie",
		58: "Badass Pixie",
		60: "Unknown",
		61: "Unknown",
		62: "Unknown",
		63: "Unknown",
		64: "Unknown",
		65: "Unknown",
		66: "Unknown",
		67: "Unknown",
		68: "Unknown",
		69: "Unknown",
		70: "Unknown",
		}
	# Dictionary of objectives (Objectives the player can complete as well as the bonus objectives)
	objectives = {
		1: "Retrieve a valuable artifact",
		2: "Eliminate a dangerous enemy leader",
		3: "Collect rare resources",
		4: "Investigate mysterious occurrences",
		5: "Rescue hostages or captured allies",
		6: "Disrupt enemy operations",
		7: "Escort a convoy or important NPC",
		8: "Secure a strategic location",
		9: "Solve puzzles or riddles",
		10: "Gather intelligence on enemy movements",
		11: "Destroy enemy infrastructure",
		12: "Protect a vulnerable target",
		13: "Retrieve stolen technology",
		14: "Defend against waves of enemies",
		15: "Survive in hostile territory for a set time",
		16: "Navigate dangerous terrain",
		17: "Assassinate high-value targets",
		18: "Break through enemy defenses",
		19: "Complete a series of trials or challenges",
		20: "Uncover hidden treasure or secrets",
		21: "Repair malfunctioning equipment",
		22: "Intercept enemy communications",
		23: "Capture enemy outposts",
		24: "Track down a notorious criminal",
		25: "Retrieve stolen data",
		26: "Rescue stranded civilians",
		27: "Disarm explosive devices",
		28: "Hunt down dangerous wildlife",
		29: "Infiltrate enemy territory undetected",
		30: "Negotiate peace between warring factions",
		31: "Retrieve lost or stolen vehicles",
		32: "Destroy enemy artillery",
		33: "Investigate a series of disappearances",
		34: "Retrieve a lost shipment",
		35: "Sabotage enemy supply lines",
		36: "Deliver critical supplies to remote outposts",
		37: "Recover valuable documents",
		38: "Assist in the construction of defensive structures",
		39: "Rescue a VIP from enemy custody",
		40: "Conduct reconnaissance on enemy positions",
		41: "Neutralize enemy spies",
		42: "Retrieve experimental technology",
		43: "Defend civilians during an evacuation",
		44: "Eliminate a rogue AI",
		45: "Navigate a treacherous maze",
		46: "Escort a group of refugees to safety",
		47: "Retrieve medical supplies from hostile territory",
		48: "Infiltrate a heavily guarded facility",
		49: "Secure a cache of weapons for the resistance",
		50: "Confront a powerful enemy in single combat"
	}
	# Dictionary of twists (The unknown twist for the quest the players do not know about)
	twists = {
		1: "Betrayal from an unexpected ally",
		2: "Unexpected reinforcements for the enemy",
		3: "A powerful boss unexpectedly appears",
		4: "The quest objective is a decoy",
		5: "Environmental hazards intensify",
		6: "A previously defeated enemy returns stronger",
		7: "The quest giver is not who they seem",
		8: "Allies turn against each other",
		9: "The quest area is trapped or rigged with explosives",
		10: "A rival faction interferes with the mission",
		11: "The objective constantly moves or changes location",
		12: "Time limit suddenly imposed",
		13: "A hidden enemy ambushes the party",
		14: "The quest item is cursed or malfunctioning",
		15: "A moral dilemma complicates the mission",
		16: "The environment itself becomes hostile",
		17: "An unexpected natural disaster strikes",
		18: "The party is split up or separated",
		19: "Illusions or mind tricks deceive the party",
		20: "The quest giver betrays the party",
		21: "The quest objective is already destroyed or gone",
		22: "An unexpected ally offers assistance",
		23: "The quest is a simulation or test",
		24: "A hidden enemy base is revealed",
		25: "The party is hunted by a relentless enemy",
		26: "The party is affected by a debilitating condition",
		27: "The quest leads to a parallel dimension or alternate reality",
		28: "A secret enemy faction is revealed",
		29: "A valuable NPC is captured or killed",
		30: "The quest area is booby-trapped",
		31: "The party is framed for a crime they didn't commit",
		32: "A powerful artifact corrupts the party",
		33: "The party is plagued by hallucinations",
		34: "The quest giver is under mind control",
		35: "The party encounters a powerful ancient creature",
		36: "The quest involves time travel or time manipulation",
		37: "A rival party competes for the same objective",
		38: "The quest objective is guarded by a powerful force field",
		39: "The party is blackmailed or threatened",
		40: "The quest leads to a hidden underground complex",
		41: "The party is infected by a deadly virus",
		42: "A betrayal is revealed within the party",
		43: "The quest area is surrounded by a deadly energy field",
		44: "The party discovers a hidden conspiracy",
		45: "The quest item is stolen by a cunning thief",
		46: "The quest leads to a parallel dimension or alternate reality",
		47: "The party is misled by false information",
		48: "A powerful artifact awakens ancient guardians",
		49: "The party must sacrifice something valuable to proceed",
		50: "A moral choice determines the outcome of the quest"
	}
	# Risk assessment level for quest (How difficult to make the quest)
	risk_level = {
		1.:"Very Easy",
		2.:"Easy",
		2.:"Normal",
		2.:"Slightly Difficult",
		2.:"Difficult",
		2.:"Slightly Hard",
		2.:"Hard",
		2.:"Very Hard",
		2.:"Insane",
		2.:"Near Impossible",
		2.:"Impossible",
		2.:"Demon",
		2.:"Satan",
	}

	# Quest reward chests
	reward_type = {
		1:"Tiny Chest",
		2:"Small Cache",
		3:"Medium Cache",
		4:"Medium Chest",
		5:"Large Cache",
		6:"Legendary Cache",
		7:"Loot Chest",
		8:"Dice Loot Chest",
	}
	
	

	bounty_board = []
	bounty_count = random.randint(1, 10)
	for i in range(bounty_count):
		# Randomly select Quest Type, Location, Enemy, Risk Level, Objective, Twist and Reward
		random_quest_type_key = random.choice(list(quest_types.keys()))
		random_quest_type = quest_types[random_quest_type_key]

		random_location_key = random.choice(list(locations.keys()))
		random_location = locations[random_location_key]

		random_enemies_key = random.choice(list(enemies.keys()))
		random_enemies = enemies[random_enemies_key]

		random_risk_level_key = random.choice(list(risk_level.keys()))
		random_risk_level = risk_level[random_risk_level_key]

		random_objective_key = random.choice(list(objectives.keys()))
		random_objective = objectives[random_objective_key]

		random_twist_key = random.choice(list(twists.keys()))
		random_twist = twists[random_twist_key]

		random_reward_key = random.choice(list(reward_type.keys()))
		random_reward = reward_type[random_reward_key]

		# Generate quest details
		quest_title = f"{random_quest_type} in {random_location}\n" #Title of the quest for BM Storage purposes
		quest_description = "Help needed! " + random_quest_type.lower() + " in the " + random_location.lower() + "." 
		quest_objective = f"Bonus objective: {random_objective}."
		quest_reward = f"Rewards: Experience,Loot and a random {random_reward}."

		#Risk assessment determines the difficulty level to make the quest
		risk_assessment = f"Risk Assessment Level : {random_risk_level}"
		possible_enemy = f"Enemy Type at Location : {random_enemies}" #most likely enemy type but not restricted to only that type
		quest_twist = f"Twist: {random_twist}" #The real kicker for the quest at hand, What kind of debuff or trick the players will have to deal with

		bounty_board.append(f"{quest_title}\n{quest_description}\n{quest_objective}\n{possible_enemy}\n{quest_reward}\n{risk_assessment}\n\n{quest_twist}")

	save_to_file("Generated_Bounty_board.txt",''.join(bounty_board))
	return bounty_board