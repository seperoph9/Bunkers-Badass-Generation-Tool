import random

def generate_potion():
	potions = {
		(1, 5): 'Common Tina Potion',
		(6, 10): 'Common Health Potion   -   Effect(1d8 Health)',
		(11, 15): 'Common Shield Potion   -   Effect(1d8 Shield)',
		(16, 20): 'Check Potion',
		(21, 25): 'Element Potion',
		(26, 30): 'Rare Tina Potion',
		(31, 35): 'Rare Health Potion   -   Effect(2d8+5 Health)',
		(36, 40): 'Rare Shield Potion   -   Effect(2d8+5 Shield)',
		(41, 45): 'Stat Potion',
		(46, 50): 'Twofer Potion',
		(51, 55): 'Epic Tina Potion',
		(56, 60): 'Epic Health potion   -   Effect(3d8+10 Health)',
		(61, 65): 'Epic Shield Potion   -   Effect(3d8+10 Shield)',
		(66, 70): 'Lucky Potion',
		(71, 75): 'Invisibility Potion',
		(76, 80): 'Legendary Tina Potion',
		(81, 85): 'Legendary Health Potion   -   Effect(4d8+20 Health)',
		(86, 90): 'Legendary Shield Potion   -   Effect(4d8+20 Shield)',
		(91, 95): 'Fumble Potion',
		(96, 100): 'Gold Farmer Potion',
	}

	tina_Potions = {
		1:'Golden Gulp',
		2:'Deadly Horrible Potion of Death',
		3:'One Liner Juice',
		4:'Best Drink Ever',
		5:'What if we were girlfriends',
		6:'Gotta Sing',
		7:'Friday Freak',
		8:'Love Potion Number 69',
		9:'Truth Serum',
		10:'No Curses Plz',
		11:'Gotta Dance',
		12:'Big Booty Potion',
		13:'Vommodrink',
		14:'Stank Drank',
		15:'Do u Feel Lucky',
		16:'Bullet Burp',
		17:'Baddie Juice',
		18:'Do you like me y/n',
		19:'Roshambo',
		20:'Punch Drunk',
		21:'Butt Farts',
		22:'Haterade',
		23:'Fancy Feats',
		24:'2 sexy for my boots',
		25:'Parent Trap',
		26:'Scrappy',
		27:'Not Today',
		28:'Liquid Confidence',
		29:'Good Touch',
		30:'Tina Tincture',
	}

	# Roll Random
	roll_result = random.randint(1, 100)

	# Force Common Tina Potion
	# roll_result = 26
	potion_roll = ''

	# Find the Corresponding Potion
	for catch in potions.keys():
		if roll_result in range(catch[0], catch[1]+1):
			potion_roll = potions[catch]
			break
	
	# Random Tina Potion Roll
	tina_roll = random.randint(1, list(tina_Potions.keys())[-1])

	# Tina Potions Specialties
	if potion_roll == 'Rare Tina Potion': # 26-30
		potion_roll = tina_Potions[min(tina_roll + 3, 30)]
	elif potion_roll == 'Epic Tina Potion': # 51-55
		potion_roll = tina_Potions[min(tina_roll + 5, 30)]
	elif potion_roll == 'Legendary Tina Potion': # 76-80
		potion_roll = tina_Potions[min(tina_roll + 10, 30)]

	return potion_roll

