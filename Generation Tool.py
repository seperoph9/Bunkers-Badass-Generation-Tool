import random
import os

# Import generator functions from separate files
from grenade_generator import generate_grenade
from relic_generator import generate_relic
from potion_generator import generate_potion
from gun_generator import generate_gun
from shield_generator import generate_shield
from cache_generator import generate_cache
from trauma_generator import generate_trauma
from enemy_loot_generator import generate_enemy_loot
from loot_chest_generator import generate_loot_chest
from dice_chest_generator import generate_dice_chest_loot
from moxx_tails_generator import generate_moxx_tails

# Define a dictionary to map user choices to generator functions
generator_functions = {
	"1": generate_gun,
	"2": generate_shield,
	"3": generate_grenade,
	"4": generate_relic,
	"5": generate_potion,
	"6": generate_cache,
	"7": generate_trauma,
	"8": generate_loot_chest,
	"9": generate_dice_chest_loot,
	"10": generate_enemy_loot,
	"11": generate_moxx_tails
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
1. Generate a Gun
2. Generate a Shield
3. Generate a Grenade
4. Generate a Relic
5. Generate a Potion
6. Generate a Cache
7. Generate a Trauma
8. Generate a Loot Chest
9. Generate a Dice Chest
10. Generate Enemy Loot
11. Generate Mox Tails Drink''')

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
			print("Generated item:")
			print(generator_functions[choice]())

		# Ask if the user wants to generate another item
		another_item = input("\nGenerate another item? (y/n): ").strip().lower()
		if 'y' not in another_item:
			clear_screen()
			break


# Entry point of the program
main()

