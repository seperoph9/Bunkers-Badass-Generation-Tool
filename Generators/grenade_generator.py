import random
def generate_grenade():
	level = int(input("What is the level requested? "))

	shields = [
		# Level 1 - 6
		["Ashen Grenade   -   (Transfusion)   -   Damage (1d8)   -   Effect (Gain Health equal to damage dealth)",
		"Dahlia Grenade   -   (Generator)   -   Damage (1d8)   -   Effect (Recharges shields equal to damage dealt)",
		"Feriore Grenade   -   (Jumping)   -   Damage (1d8)   -   Effect (Detonates then jumps 2 squares and jumps again)",
		"Hyperius Grenade   -   (Longbow)   -   Damage (1d8)   -   Effect (Teleports to target and ignores cover)",
		"Malefactor Grenade   -   (Elemental)   -   Damage (1d8)   -   Effect (Gains element type)",
		"Pangoblin Grenade   -   (Rubberized)   -   Damage (1d8)   -   Effect (Bounce off surfaces, Detonates on contact with any enemy)",
		"Stoker Grenade   -   (Proximity Mine)   -   Damage (1d8)   -   Effect (Wont detonate until enemy is in adjacent tile)",
		"Torgue Grenade   -   (Splash)   -   Damage(1d8)   -   Effect (Deals full spash damage)"],
		
		# Level 7 - 12
		["Ashen Grenade   -   (Homing)   -   Damage (2d8)   -   Effect (Gain Health equal to damage dealth)",
		"Dahlia Grenade   -   (Bouncing Betty)   -   Damage (2d8)   -   Effect (Recharges shields equal to damage dealt)",
		"Feriore Grenade   -   (Sticky)   -   Damage (2d8)   -   Effect (Detonates then jumps 2 squares and jumps again)",
		"Hyperius Grenade   -   (Raider)   -   Damage (2d10)   -   Effect (Teleports to target and ignores cover)",
		"Malefactor Grenade   -   (Contact)   -   Damage (2d8)   -   Effect ( Gains element type)",
		"Pangoblin Grenade   -   (Force)   -   Damage (2d8)   -   Effect (Bounce off surfaces, Detonates on contact with any enemy)",
		"Stoker Grenade   -   (Rain)   -   Damage (2d8)   -   Effect (Wont detonate until enemy is in adjacent tile)",
		"Torgue Grenade   -   (Mirv)   -   Damage(2d8)   -   Effect (Deals full spash damage)"],

		# Level 13 - 18
		["Ashen Grenade   -   (Transfusion)   -   Damage (3d8)   -   Effect (Gain Health equal to damage dealth)",
		"Dahlia Grenade   -   (Generator)   -   Damage (3d8)   -   Effect (Recharges shields equal to damage dealt)",
		"Feriore Grenade   -   (Jumping)   -   Damage (3d8)   -   Effect (Detonates then jumps 2 squares and jumps again)",
		"Hyperius Grenade   -   (Longbow)   -   Damage (1d8)   -   Effect (Teleports to target and ignores cover)",
		"Malefactor Grenade   -   (Elemental)   -   Damage (3d8)   -   Effect ( Gains element type)",
		"Pangoblin Grenade   -   (Rubberized)   -   Damage (3d8)   -   Effect (Bounce off surfaces, Detonates on contact with any enemy)",
		"Stoker Grenade   -   (Proximity Mine)   -   Damage (3d8)   -   Effect (Wont detonate until enemy is in adjacent tile)",
		"Torgue Grenade   -   (Splash)   -   Damage(3d8)   -   Effect (Deals full spash damage)"],	

		# Level 19 - 24
		["Ashen Grenade   -   (Homing)   -   Damage (4d8)   -   Effect (Gain Health equal to damage dealth)",
		"Dahlia Grenade   -   (Bouncing Betty)   -   Damage (4d8)   -   Effect (Recharges shields equal to damage dealt)",
		"Feriore Grenade   -   (Sticky)   -   Damage (4d8)   -   Effect (Detonates then jumps 2 squares and jumps again)",
		"Hyperius Grenade   -   (Raider)   -   Damage (4d10)   -   Effect (Teleports to target and ignores cover)",
		"Malefactor Grenade   -   (Contact)   -   Damage (4d8)   -   Effect ( Gains element type)",
		"Pangoblin Grenade   -   (Force)   -   Damage (4d8)   -   Effect (Bounce off surfaces, Detonates on contact with any enemy)",
		"Stoker Grenade   -   (Rain)   -   Damage (4d8)   -   Effect (Wont detonate until enemy is in adjacent tile)",
		"Torgue Grenade   -   (Mirv)   -   Damage(4d8)   -   Effect (Deals full spash damage)"],

		# Level 25 - 30
		["Ashen Grenade   -   (Transfusion)   -   Damage (5d8)   -   Effect (Gain Health equal to damage dealth)",
		"Dahlia Grenade   -   (Generator)   -   Damage (5d8)   -   Effect (Recharges shields equal to damage dealt)",
		"Feriore Grenade   -   (Jumping)   -   Damage (5d8)   -   Effect (Detonates then jumps 2 squares and jumps again)",
		"Hyperius Grenade   -   (Longbow)   -   Damage (5d8)   -   Effect (Teleports to target and ignores cover)",
		"Malefactor Grenade   -   (Elemental)   -   Damage (5d8)   -   Effect ( Gains element type)",
		"Pangoblin Grenade   -   (Rubberized)   -   Damage (5d8)   -   Effect (Bounce off surfaces, Detonates on contact with any enemy)",
		"Stoker Grenade   -   (Proximity Mine)   -   Damage (5d8)   -   Effect (Wont detonate until enemy is in adjacent tile)",
		"Torgue Grenade   -   (Splash)   -   Damage(5d8)   -   Effect (Deals full spash damage)"]
	]

	# Get Random roll
	grenade_roll = random.randint(0, 7)

	if level in range(1, 7):
		return shields[0][grenade_roll]
	elif level in range(7, 13):
		return shields[1][grenade_roll]
	elif level in range(13, 19):
		return shields[2][grenade_roll]
	elif level in range(19, 25):
		return shields[3][grenade_roll]
	elif level in range(25, 31):
		return shields[4][grenade_roll]