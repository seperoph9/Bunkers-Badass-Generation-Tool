import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file



def generate_random_boss():
	# List of possible boss names
	boss_names = [
    "Captain Scarlett",
    "Captain Traunt",
    "Warden",
    "Mouthpiece",
    "Gigamind",
    "Graveward",
    "Killavolt",
    "Troy Calypso",
    "Tyreen Calypso",
    "Katagawa Ball",
    "Billy, the Anointed",
    "Kategawa Jr.",
    "Agonizer 9000",
    "Pain and Terror",
    "Katagawa, the Tyrant",
    "Aurelia Hammerlock",
    "The Rampager",
    "The Agonizer 9000",
    "Troy and Tyreen",
    "The Graveward",
    "Handsome Sorcerer",
    "Scourge the Invincible Martyr",
    "Master Gee the Invincible",
    "Pyro Pete the Invincible",
    "Voracidous the Invincible",
    "Hyperius the Invincible",
    "Dexiduous the Invincible",
    "Terramorphous the Invincible",
    "Son of Crawmerax",
    "Shadow of Terramorphous",
    "Haderax the Invincible",
    "Vermivorous the Invincible",
    "Omnd-Omnd-Ohk",
    "Badassaurus Rex",
    "Scorch",
    "Knuckle Dragger",
    "The Warrior",
    "Bloodwing",
    "Saturn",
    "Wilhelm",
    "JACKenstein",
    "Master Gee",
    "Voracidous",
    "Hyperius",
    "Dexiduous",
    "Son of Mothrakk",
    "Piston",
    "Jack's Body Double"
]
	# List of possible boss types
	boss_types = ["Humanoid", "Creature", "Robot", "Mutant", "Alien"]

	# List of possible boss abilities
	boss_abilities = [
    "Fire Breath",
    "Electric Shock",
    "Summon Minions",
    "Ground Pound",
    "Energy Beam",
    "Teleportation",
    "Regeneration",
    "Explosive Nova",
    "Elemental Barrage",
    "Laser Barrage",
    "Cryo Blast",
    "Toxic Spray",
    "Shockwave Slam",
    "Gravity Manipulation",
    "Sonic Scream",
    "Phase Shift",
    "Corrosive Vomit",
    "Berserker Rage",
    "Siphon Life",
    "Mind Control",
    "Summon Turret",
    "Meteor Shower",
    "Dimensional Rift",
    "Time Manipulation",
    "Adaptive Shielding",
    "Telekinesis",
    "Plasma Blast",
    "Acid Rain",
    "Shrapnel Storm",
    "Psychic Blast",
    "Spectral Summoning",
    "Ethereal Form",
    "Darkness Veil",
    "Chaos Infusion",
    "Molten Core",
    "Charged Strike",
    "Blinding Flash",
    "Shadow Step",
    "Frostbite Aura",
    "Vampiric Drain",
    "Venomous Bite",
    "Unholy Resurrection",
    "Explosive Detonation",
    "Poison Gas Cloud",
    "Spectral Projection",
    "Supernova Burst",
    "Soul Drain",
    "Arcane Blast"
]

	# List of possible boss weaknesses
	boss_weaknesses = [
    "Explosive Damage",
    "Corrosive Damage",
    "Fire Damage",
    "Shock Damage",
    "Cryo Damage",
    "Radiation Damage",
    "Critical Hits to Weak Spots",
    "Melee Attacks",
    "Elemental Vulnerability",
    "High Velocity Projectiles",
    "EMP Pulses",
    "Status Effects",
    "Disabling Shields",
    "Disabling Armor",
    "Disabling Weapons",
    "Environmental Hazards",
    "Evasion Techniques",
    "Mobility Restriction",
    "Pain Sensitivity",
    "Psychological Manipulation",
    "Teleportation Interruption",
    "Limited Vision",
    "Sensory Overload",
    "Energy Drain",
    "Disrupted Phasing",
    "Physical Exhaustion",
    "Psychic Resonance",
    "Spectral Disruption",
    "Moral Weakness",
    "Fear Induction",
    "Confusion State",
    "Elemental Instability",
    "Disrupted Healing",
    "Vulnerability to Light",
    "Vulnerability to Sound",
    "Vulnerability to Cold",
    "Vulnerability to Heat",
    "Vulnerability to Radiation",
    "Vulnerability to Acid",
    "Vulnerability to Poison",
    "Vulnerability to Electricity",
    "Vulnerability to Magnetism",
    "Vulnerability to Kinetic Force",
    "Vulnerability to Psychic Attacks",
    "Vulnerability to Sonic Waves",
    "Vulnerability to Energy Waves",
    "Vulnerability to Dark Magic"
]

	# List of possible boss loot drops
	boss_loot = ["Legendary Weapon", "Legendary Cache", "Large Cache Per player"]

	# Select random attributes for the boss
	name = random.choice(boss_names)
	boss_names.remove(name)  # Ensure unique names
	boss_type = random.choice(boss_types)
	boss_ability = random.choice(boss_abilities)
	boss_weakness = random.choice(boss_weaknesses)
	loot_drop = random.choice(boss_loot)

	# Generate boss description
	description = f"The {boss_type} boss named {name} is known for its {boss_ability} ability. Its weakness is {boss_weakness.lower()}."

	# Construct boss dictionary
	boss = {
		"Name": name,
		"Type": boss_type,
		"Description": description,
		"Abilities": [boss_ability],
		"Weaknesses": [boss_weakness],
		"Loot Drops": [loot_drop]
	}
	# Save the boss to a file
	save_boss_to_file(boss, "generated_boss.txt")
	return boss

def save_boss_to_file(boss, filename):
	with open(filename, 'w') as file:
		for key, value in boss.items():
			file.write(f"{key}: {value}\n")



