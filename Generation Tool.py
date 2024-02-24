import random
import os

# Import generator functions from separate files
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.cache_generator import generate_cache
from Generators.trauma_generator import generate_trauma
from Generators.enemy_loot_generator import generate_enemy_loot
from Generators.loot_chest_generator import generate_loot_chest
from Generators.dice_chest_generator import generate_dice_chest_loot
from Generators.moxx_tails_generator import generate_moxx_tails
from Generators.world_event_generator import generate_world_event
from Generators.combat_scenario_generator import generate_combat_scenario
from Generators.bounty_board_generator import generate_bounty_board
from Generators.quest_generator import generate_random_quest

# Define a dictionary to map user choices to generator functions
generator_functions = {
	"1": generate_gun, 
	"2": generate_shield,
	"3": generate_grenade,
	"4": generate_relic,
	"5": generate_potion,
	"6": generate_cache,
	"7": generate_trauma, #Generate a trauma that the player recieves
	"8": generate_loot_chest,
	"9": generate_dice_chest_loot,
	"10": generate_enemy_loot,
	"11": generate_moxx_tails,
	"12": generate_combat_scenario, # Generates a combat scenario to use
	"13": generate_random_quest, # Same as the bounty board but an individual quest
	# "14": generate_custom_npc,
	# "15": generate_custom_boss,
	# "16": generate_environmental_hazard,
	"17": generate_bounty_board, # Generates a bounty board full of quests for the party to choose from
	"18": generate_world_event,
	# "19": generate_tavern_tale,
	# "20": generate_trap,
	# "21": generate_puzzle,
	# "22": generate_random_encounter,
	# "23": generate_arena_challenge,
}

# Function to clear the screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

# Function to get user choice with validation
def get_user_choice(prompt, options):
	while True:
		choice = input(prompt).strip()
		if choice in options:
			return choice
		print("Invalid choice. Please try again.")

# Main function to run the program
def main():
	while True:
		# Display the menu options to the user
		print('''Choose an option:
1.  Generate a Gun			2.  Generate a Shield			3.  Generate a Grenade
4.  Generate a Relic			5.  Generate a Potion			6.  Generate a Cache	
7.  Generate a Trauma			8.  Generate a Loot Chest		9.  Generate a Dice Chest	
10. Generate Enemy Loot			11. Generate Mox Tails Drink		12. Generate a Combat Scenario	
13. Generate a custom quest		14. Generate a custom NPC		15. Generate a Custom Boss	
16. Generate a Environmental Hazard 	17. Generate a Bounty Board 		18. Generate a Random World Event	
19. Generate a Tavern Tale    		20. Generate a Random Trap		21. Generate a Random Puzzle  
22. Generate a Random Encounter		23. Generate a Arena Challenge''')

		# Get user choice
		choice = get_user_choice("Enter your choice: ", generator_functions.keys())
		clear_screen()

		if choice == "6": # Cache Prompt
			cache_type = get_user_choice(('''Enter a Cache type:
1. Single/Tiny Chest
2. Small Cache
3. Medium Cache
4. Medium Chest
5. Large Cache
6. Legendary Cache'''),
				["1", "2", "3", "4", "5", "6"])
			# Generate and display cache items
			print(generator_functions[choice](int(cache_type)))
		elif choice == "1": # Gun Prompt
			gentype = input("Completely Random(1) or a certain Rarity(2)? ")
			clear_screen()
			if gentype == "1": # Generate a random gun
				checkrarity = 0
				print("Generated item:", generate_gun(checkrarity))
			elif gentype == "2": # Get Rarity
				checkrarity = input("Enter a rarity: Common(1) Uncommon(2) Rare(3) Epic(4) Legendary(5): ")
				clear_screen()
				print("Generated item:", generate_gun(checkrarity))


		elif choice == "4": # Relic Prompt
			gentype = input("Completely Random(1) or a certain Rarity(2)? ")
			clear_screen()
			if gentype == "1": # Generate a Relic gun
				checkrarity = 0
				print("Generated item:", generate_relic(checkrarity))
			elif gentype == "2": # Get Rarity
				checkrarity = input("Enter a rarity: Common(1) Uncommon(2) Rare(3): ")
				clear_screen()
				print("Generated item:", generate_relic(checkrarity))
		else:
			# For other choices, simply generate and display the item
			print(generator_functions[choice]())

		# Ask if the user wants to generate another item
		another_item = input("\nGenerate another item? (y/n): ").strip().lower()
		if 'y' not in another_item:
			clear_screen()
			break


# Entry point of the program
main()




#To do
# A combat Scenario Creator
# A Quest Generator
# A NPC Generator
# A Boss Generator
# A Environmental  Hazard Chance Generator
# A Bounty Board Generator
# A World Event Generator
# A Tavern Tale Generator (Possibly Tie to quest Generator)
# A Trap Generator
# A Random Encounter Generator
# A Puzzle Generator
# A Arena Challenge Generator
# A Legendary Encounter Generator (Would be tied with the random encounter generator)