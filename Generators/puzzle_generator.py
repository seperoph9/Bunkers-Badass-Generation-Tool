import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file


def generate_random_puzzle():
	# Dictionary of puzzles with hints and solutions
	puzzles = {
		1: {
			"puzzle": "Color Lock Puzzle: Players must arrange colored tiles or gems in a specific order to unlock a door or chest.",
			"hint": "Hint: Pay attention to the colors and their positions.",
			"solution": "Solution: Red, Blue, Green, Yellow."
		},
		2: {
			"puzzle": "Symbol Matching Puzzle: Players must match symbols or runes to their corresponding locations to unlock a mechanism.",
			"hint": "Hint: Each symbol corresponds to a specific location.",
			"solution": "Solution: Match the symbols to the symbols on the mechanism."
		},
		3: {
			"puzzle": "Cipher Puzzle: Players must decode a hidden message or riddle to uncover the solution to the puzzle.",
			"hint": "Hint: Look for patterns or repeated symbols in the cipher.",
			"solution": "Solution: 'The key to success is hidden in plain sight.'"
		},
		4: {
			"puzzle": "Logic Gate Puzzle: Players must manipulate logic gates to control the flow of energy or unlock a door.",
			"hint": "Hint: Experiment with different combinations of logic gates.",
			"solution": "Solution: Use an AND gate followed by an OR gate."
		},
		5: {
			"puzzle": "Pattern Recognition Puzzle: Players must identify and replicate a complex pattern or sequence to progress.",
			"hint": "Hint: Break the pattern down into smaller segments.",
			"solution": "Solution: The pattern alternates between squares and circles."
		},
		6: {
			"puzzle": "Maze Puzzle: Players must navigate through a labyrinthine maze to reach the exit.",
			"hint": "Hint: Keep track of your movements and explore all possible paths.",
			"solution": "Solution: Follow the left-hand wall until you reach the exit."
		},
		7: {
			"puzzle": "Rotating Tile Puzzle: Players must rotate tiles or panels to create a clear path or reveal a hidden passage.",
			"hint": "Hint: Start by rotating the outermost tiles.",
			"solution": "Solution: Rotate the tiles clockwise starting from the top left."
		},
		8: {
			"puzzle": "Weighted Pressure Plate Puzzle: Players must place objects of varying weights on pressure plates to trigger mechanisms.",
			"hint": "Hint: Try different combinations of objects to find the correct weight.",
			"solution": "Solution: Place the heavy object on the left plate and the light object on the right plate."
		},
		9: {
			"puzzle": "Mirror Reflection Puzzle: Players must manipulate mirrors or reflective surfaces to direct beams of light to specific points.",
			"hint": "Hint: Use the mirrors to redirect the beams of light.",
			"solution": "Solution: Angle the mirrors to reflect the light onto the target."
		},
		10: {
			"puzzle": "Music Puzzle: Players must play or replicate a musical tune on a set of instruments to unlock a door or chest.",
			"hint": "Hint: Listen carefully to the melody and replicate it on the instruments.",
			"solution": "Solution: Play the notes C, E, G on the piano."
		},
		11: {
			"puzzle": "Memory Puzzle: Players must memorize and repeat a sequence of buttons, symbols, or colors to progress.",
			"hint": "Hint: Start with a small sequence and gradually increase the difficulty.",
			"solution": "Solution: Red, Green, Blue, Yellow."
		},
		12: {
			"puzzle": "Alchemy Puzzle: Players must mix and combine different ingredients or elements to create potions or unlock doors.",
			"hint": "Hint: Experiment with different combinations of ingredients.",
			"solution": "Solution: Mix one part mandrake root with two parts water."
		},
		13: {
			"puzzle": "Word Riddle Puzzle: Players must solve a riddle or cryptic message involving words or language to proceed.",
			"hint": "Hint: Break the riddle down into smaller parts and look for hidden clues.",
			"solution": "Solution: The answer is 'fire.'"
		},
		14: {
			"puzzle": "Gear Rotation Puzzle: Players must rotate gears or mechanisms to align them and activate a mechanism.",
			"hint": "Hint: Start by aligning the gears closest to the target.",
			"solution": "Solution: Rotate the gear on the left clockwise and the gear on the right counterclockwise."
		},
		15: {
			"puzzle": "Hieroglyph Puzzle: Players must decipher and interpret ancient hieroglyphics to uncover the solution.",
			"hint": "Hint: Look for common symbols and their meanings.",
			"solution": "Solution: The hieroglyph for 'sun' represents the letter 'A'."
		},
		16: {
			"puzzle": "Crystal Alignment Puzzle: Players must arrange crystals or gemstones in a specific alignment to unlock a mechanism.",
			"hint": "Hint: Experiment with different arrangements until you find the correct alignment.",
			"solution": "Solution: Arrange the crystals in a circle with the red crystal in the center."
		},
		17: {
			"puzzle": "Statue Puzzle: Players must interact with statues or sculptures in a specific sequence to unlock a door or passage.",
			"hint": "Hint: Look for clues in the environment or on the statues themselves.",
			"solution": "Solution: Activate the statues in the order they appear in the mural."
		},
		18: {
			"puzzle": "Tangram Puzzle: Players must arrange geometric shapes to form a specific pattern or image.",
			"hint": "Hint: Start by fitting the larger shapes together.",
			"solution": "Solution: Arrange the shapes to form a square."
		},
		19: {
			"puzzle": "Logic Puzzle: Players must solve a complex logic problem or grid puzzle to unlock a mechanism.",
			"hint": "Hint: Break the puzzle down into smaller parts and solve each part individually.",
			"solution": "Solution: The blue house is next to the green house."
		},
		20: {
			"puzzle": "Time Puzzle: Players must manipulate time-related mechanisms or solve time-based challenges to progress.",
			"hint": "Hint: Experiment with different time-related actions and their consequences.",
			"solution": "Solution: Activate the time crystal to reverse time and open the door."
		},
		21: {
			"puzzle": "Chess Puzzle: Players must solve a chess puzzle involving specific moves or strategies to unlock a mechanism.",
			"hint": "Hint: Think several moves ahead and look for opportunities to create checkmate.",
			"solution": "Solution: Move the rook to threaten the opponent's king."
		},
		22: {
			"puzzle": "Dice Puzzle: Players must roll dice or solve a dice-related challenge to proceed.",
			"hint": "Hint: Pay attention to the numbers on the dice and their positions.",
			"solution": "Solution: Roll a double six to unlock the door."
		},
		23: {
			"puzzle": "Sudoku Puzzle: Players must solve a Sudoku puzzle to unlock a door or chest.",
			"hint": "Hint: Start with the empty squares and work your way through the puzzle.",
			"solution": "Solution: The numbers 1 through 9 must appear in each row, column, and 3x3 grid."
		},
		24: {
			"puzzle": "Lever Puzzle: Players must pull levers or switches in a specific sequence to unlock a mechanism.",
			"hint": "Hint: Start with the levers closest to the mechanism and work your way out.",
			"solution": "Solution: Pull the levers from left to right."
		},
		25: {
			"puzzle": "Crystal Maze Puzzle: Players must navigate through a maze filled with crystal obstacles and challenges.",
			"hint": "Hint: Look for patterns in the crystal formations to find the correct path.",
			"solution": "Solution: Follow the path of the blue crystals."
		},
		26: {
			"puzzle": "Pipes Puzzle: Players must connect pipes or conduits to redirect energy flow and unlock a mechanism.",
			"hint": "Hint: Start by connecting the pipes closest to the energy source.",
			"solution": "Solution: Connect the pipes to create a continuous flow of energy."
		},
		27: {
			"puzzle": "Tarot Card Puzzle: Players must interpret and arrange tarot cards in a specific order to unlock a mechanism.",
			"hint": "Hint: Each card represents a different aspect of the puzzle.",
			"solution": "Solution: Arrange the cards in ascending order from left to right."
		},
		28: {
			"puzzle": "Circuit Puzzle: Players must complete electrical circuits or connections to activate a mechanism.",
			"hint": "Hint: Look for loose wires or incomplete circuits that need to be connected.",
			"solution": "Solution: Connect the red wire to the blue wire to complete the circuit."
		},
		29: {
			"puzzle": "Laser Puzzle: Players must redirect laser beams using mirrors or prisms to unlock a mechanism.",
			"hint": "Hint: Experiment with different angles and positions for the mirrors.",
			"solution": "Solution: Angle the mirrors to reflect the laser beam onto the target."
		},
		30: {
			"puzzle": "Pattern Lock Puzzle: Players must input a specific sequence or pattern on a lock mechanism to unlock it.",
			"hint": "Hint: Look for clues in the environment or on the lock itself.",
			"solution": "Solution: Input the pattern shown on the nearby mural."
		},
		31: {
			"puzzle": "Chessboard Puzzle: Players must navigate a chessboard-like grid with specific rules or challenges.",
			"hint": "Hint: Each square on the chessboard has different properties.",
			"solution": "Solution: Avoid the squares with traps and hazards."
		},
		32: {
			"puzzle": "Crystal Ball Puzzle: Players must gaze into crystal balls or scrying pools to reveal hidden clues or solutions.",
			"hint": "Hint: Focus your attention on the crystal ball and clear your mind.",
			"solution": "Solution: The crystal ball reveals the location of the hidden key."
		},
		33: {
			"puzzle": "Clock Puzzle: Players must manipulate clock mechanisms or solve time-related challenges to progress.",
			"hint": "Hint: Look for clues related to time and the passage of time.",
			"solution": "Solution: Set the clock to midnight to unlock the door."
		},
		34: {
			"puzzle": "Gear Puzzle: Players must arrange gears or cogwheels to create a functional mechanism.",
			"hint": "Hint: Start by aligning the gears closest to the target.",
			"solution": "Solution: Rotate the gears to connect the central gear to the target."
		},
		35: {
			"puzzle": "Memory Match Puzzle: Players must match pairs of symbols or images hidden beneath tiles or cards.",
			"hint": "Hint: Start by flipping over two tiles at a time and try to remember their positions.",
			"solution": "Solution: Match all pairs of symbols to reveal the hidden image."
		},
		36: {
			"puzzle": "Crystal Labyrinth Puzzle: Players must navigate through a labyrinth filled with crystal obstacles and challenges.",
			"hint": "Hint: Keep track of your movements and explore all possible paths.",
			"solution": "Solution: Follow the path of the green crystals to reach the exit."
		},
		37: {
			"puzzle": "Astrology Puzzle: Players must interpret celestial patterns or align astrological symbols to unlock a mechanism.",
			"hint": "Hint: Look for connections between the celestial bodies and the symbols on the mechanism.",
			"solution": "Solution: Align the symbols with the corresponding constellations."
		},
		38: {
			"puzzle": "Chessboard Maze Puzzle: Players must navigate through a maze with chessboard-like patterns and challenges.",
			"hint": "Hint: Use the chessboard pattern to plan your movements.",
			"solution": "Solution: Move in an L-shape pattern to navigate the maze."
		},
		39: {
			"puzzle": "Jigsaw Puzzle: Players must assemble pieces of a jigsaw puzzle to reveal a hidden image or clue.",
			"hint": "Hint: Look for pieces with straight edges and corners to start with.",
			"solution": "Solution: Assemble the pieces to form the image of a key."
		},
		40: {
			"puzzle": "Clockwork Puzzle: Players must manipulate clockwork mechanisms or solve clock-related challenges to progress.",
			"hint": "Hint: Look for clues related to gears, springs, and other clockwork components.",
			"solution": "Solution: Wind the clock to activate the mechanism."
		},
		41: {
			"puzzle": "Candle Puzzle: Players must interact with candles or torches in a specific sequence to unlock a mechanism.",
			"hint": "Hint: Pay attention to the position and color of each candle or torch.",
			"solution": "Solution: Light the candles in the order of the rainbow colors."
		},
		42: {
			"puzzle": "Crystal Memory Puzzle: Players must memorize and replicate a sequence of illuminated crystals to unlock a mechanism.",
			"hint": "Hint: Start with a small sequence and gradually increase the difficulty.",
			"solution": "Solution: Red, Green, Blue, Yellow, Purple."
		},
		43: {
			"puzzle": "Alchemy Circle Puzzle: Players must arrange alchemical symbols or ingredients within a circle to unlock a mechanism.",
			"hint": "Hint: Look for clues related to alchemical processes and symbols.",
			"solution": "Solution: Place the ingredients in the order of the alchemical process."
		},
		44: {
			"puzzle": "Crystal Obelisk Puzzle: Players must activate crystal obelisks in a specific sequence to unlock a mechanism.",
			"hint": "Hint: Look for clues related to the colors and positions of the obelisks.",
			"solution": "Solution: Activate the obelisks in the order of the rainbow colors."
		},
		45: {
			"puzzle": "Eclipse Puzzle: Players must manipulate light and shadow to reveal hidden symbols or patterns.",
			"hint": "Hint: Use objects to block or redirect the light to create shadows.",
			"solution": "Solution: Use the sundial to cast a shadow on the symbol."
		},
		46: {
			"puzzle": "Gearbox Puzzle: Players must manipulate gearboxes or gear mechanisms to unlock a mechanism.",
			"hint": "Hint: Start by aligning the gears closest to the target.",
			"solution": "Solution: Rotate the gears to connect the central gear to the target."
		},
		47: {
			"puzzle": "Orb Puzzle: Players must manipulate floating orbs or spheres to unlock a mechanism.",
			"hint": "Hint: Experiment with different movements and positions for the orbs.",
			"solution": "Solution: Move the orbs to align them with the corresponding symbols."
		},
		48: {
			"puzzle": "Sundial Puzzle: Players must adjust a sundial to cast a shadow on a specific symbol or location.",
			"hint": "Hint: Pay attention to the position of the sun and the direction of the shadows.",
			"solution": "Solution: Rotate the sundial until the shadow falls on the symbol."
		},
		49: {
			"puzzle": "Totem Puzzle: Players must arrange totem poles or statues in a specific order to unlock a mechanism.",
			"hint": "Hint: Look for clues related to the symbols or colors on the totems.",
			"solution": "Solution: Arrange the totems in ascending order of height."
		},
		50: {
			"puzzle": "Waterwheel Puzzle: Players must manipulate waterwheels or water mechanisms to unlock a mechanism.",
			"hint": "Hint: Look for valves or controls to adjust the flow of water.",
			"solution": "Solution: Redirect the flow of water to power the waterwheel."
		}
	}
		
	Puzzle_Manifest = []
	Puzzle_Count = random.randint(2, 10)  # Randomly choose the number of puzzles between 2 and 10
	for i in range(Puzzle_Count):
		random_puzzle_key = random.choice(list(puzzles.keys()))
		random_puzzle = puzzles[random_puzzle_key]
		# Append puzzle, hint, solution, and a blank line
		Puzzle_Manifest.append(random_puzzle["puzzle"])
		Puzzle_Manifest.append(random_puzzle["hint"])
		Puzzle_Manifest.append(random_puzzle["solution"])
		Puzzle_Manifest.append("")  # Add a blank line after the solution

	with open("Generated_Puzzles.txt", "w") as file:
		for item in Puzzle_Manifest:
			file.write(f"{item}\n")

	return Puzzle_Manifest
