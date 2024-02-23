import random

# 
# Generate Shield
# 
def generate_shield():
	level= int(input("What is the level requested? "))
	
	level1_6 = {
		#Dahlia Shield - Capacity (30) - Recharge Rate (10) - Effect (1d4 Corrosive Resistance)

		1: "Ashen Shield  -  Capacity (30) -  Shield Recharge (15) -  Effect (Fast Recharge Rate)",
		2: "Alas Shield   -   Capacity (30)  -   Shield Recharge (10)  -   Effect (1d4 Shock Resistance)",
		3: "Dahlia Shield   -   Capacity (30)  -   Shield Recharge (10)  -   Effect (1d4 Corrosive Resistance)",
		4: "Feriore Shield   -   Capacity (30)  -   Shield Recharge (10)  -   Effect (1d4 Health Regen per recharge)",
		5: "Malefactor Shield   -   Capacity(30)  -   Shield Recharge (10)  -   Effect (When depleted 1d6 shock damage to ANY adjacent targets)",
		6: "Pangoblin Shield   -   Capacity(40)  -   Shield Recharge (10)  -   Effect (High Capacity)",
		7: "Stoker Shield   -   Capacity (30)  -   Shield Recharge (10)  -   Effect (When depleted 1d6 incendiary damage to ANY adjacent targets)",
		8: "Torgue Shield   -   Capacity (30)  -   Shield Recharge (10)  -   Effect (Gain 10 max health)"
	}
	level7_12 = {
		1: "Ashen Shield   -   Capacity (55)  -   Shield Recharge (20)  -   Effect (Fast Recharge Rate)",
		2: "Alas Shield   -   Capacity (55)  -   Shield Recharge (20)  -   Effect (1d6 Shock Resistance)",
		3: "Dahlia Shield   -   Capacity (55)  -   Shield Recharge (15)  -   Effect (1d6 Corrosive Resistance)",
		4: "Feriore Shield   -   Capacity (50)  -   Shield Recharge (15)  -   Effect (1d6 Health Regen per recharge)",
		5: "Malefactor Shield   -   Capacity(50)  -   Shield Recharge (15)  -   Effect (When depleted 1d6 shock damage to ANY adjacent targets)",
		6: "Pangoblin Shield   -   Capacity(40)  -   Shield Recharge (10)  -   Effect (High Capacity)",
		7: "Stoker Shield   -   Capacity (50)  -   Shield Recharge (15)  -   Effect (When depleted 2d6 incendiary damage to ANY adjacent targets)",
		8: "Torgue Shield   -   Capacity (50)  -   Shield Recharge (15)  -   Effect (Gain 20 max health)"
	}
	level13_18 = {
		1: "Ashen Shield   -   Capacity (70)  -   Shield Recharge (25)  -   Effect (Fast Recharge Rate)",
		2: "Alas Shield   -   Capacity (70)  -   Shield Recharge (20)  -   Effect (1d10 Shock Resistance)",
		3: "Dahlia Shield   -   Capacity (75)  -   Shield Recharge (20)  -   Effect (1d10 Corrosive Resistance)",
		4: "Feriore Shield   -   Capacity (70)  -   Shield Recharge (20)  -   Effect (1d8 Health Regen per recharge)",
		5: "Malefactor Shield   -   Capacity(70)  -   Shield Recharge (20)  -   Effect (When depleted 3d6 shock damage to ANY adjacent targets)",
		6: "Pangoblin Shield   -   Capacity(80)  -   Shield Recharge (20)  -   Effect (High Capacity)",
		7: "Stoker Shield   -   Capacity (70)  -   Shield Recharge (20)  -   Effect (When depleted 3d6 incendiary damage to ANY adjacent targets)",
		8: "Torgue Shield   -   Capacity (70)  -   Shield Recharge (20)  -   Effect (Gain 30 max health)"
	}
	level19_24 = {
		1: "Ashen Shield   -   Capacity (70)  -   Shield Recharge (15)  -   Effect (Gaint +10 health and +3 melee damage while equiped)",
		2: "Alas Shield   -   Capacity (60)  -   Shield Recharge (10)  -   Effect (Roll percent dice for each incoming attack on a 60%+ take half damage)",
		3: "Dahlia Shield   -   Capacity (80)  -   Shield Recharge (10)  -   Effect (When depleted during an encounter drops 20 gold)",
		4: "Feriore Shield   -   Capacity (70)  -   Shield Recharge (20)  -   Effect (Recharge 5 shield at the start of each round)",
		5: "Malefactor Shield   -   Capacity(70)  -   Shield Recharge (15)  -   Effect (When depleted pulls targets up to 3 squares away into an adjaced square then deals 4d6 shock damage to adjacent targets)",
		6: "Pangoblin Shield   -   Capacity(100)  -   Shield Recharge (20)  -   Effect (Reduces movement to 2 squares unless depleted)",
		7: "Stoker Shield   -   Capacity (70)  -   Shield Recharge (15)  -   Effect (shock damage recharges sheidld instead of damaging it)",
		8: "Torgue Shield   -   Capacity (75)  -   Shield Recharge (15)  -   Effect (insults an enemy as mr torgue each turn dealing 1d4 psyic mockery damage and taunting the enemy)"
	}
	level25_30 = {
		1: "Ashen Shield   -   Capacity (60)  -   Shield Recharge (10)  -   Effect (gain 30 health and +10 health regen while equiped)",
		2: "Alas Shield   -   Capacity (0)  -   Shield Recharge (0)  -   Effect (roll percent dice for each incoming attack on a 70%+ take no damage)",
		3: "Dahlia Shield   -   Capacity (80)  -   Shield Recharge (15)  -   Effect (when depleted spawns 3 grenades into adjacent squares that take 3d6 shock damage)",
		4: "Feriore Shield   -   Capacity (60)  -   Shield Recharge (20)  -   Effect (when depleted toss like a grenade dealing 3d8 damage then returning)",
		5: "Malefactor Shield   -   Capacity(80)  -   Shield Recharge (15)  -   Effect (deals 2d6 incendiary damage to adjacent squares each turn while depleted)",
		6: "Pangoblin Shield   -   Capacity(60)  -   Shield Recharge (10)  -   Effect (gain +4 DMG Mod to ranged attacks while not depleted)",
		7: "Stoker Shield   -   Capacity (80)  -   Shield Recharge (15)  -   Effect (Launches 3 corrosive spikes at the target if you take 10 or more damage from a attack each spike deals 1d6 corrosive damage)",
		8: "Torgue Shield   -   Capacity (80)  -   Shield Recharge (15)  -   Effect (when depleted creates a 3x3 square area blast dealing 3d6 explosive damage and causing knockback)"
	}

	grenade_roll = random.randint(1, 8)

	if level in range(1, 7):
		return level1_6[grenade_roll]
	elif level in range(7, 13):
		return level7_12[grenade_roll]
	elif level in range(13, 19):
		return level13_18[grenade_roll]
	elif level in range(18, 25):
		return level19_24[grenade_roll]
	elif level in range(25, 31):
		return level25_30[grenade_roll]
