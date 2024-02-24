import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file


def generate_random_trap():
	traps = {
		1: "Explosive Minefield: A field of hidden explosives that detonate upon contact.",
		2: "Electric Tripwire: A wire rigged with electricity that shocks anyone who triggers it.",
		3: "Pitfall Trap: A hidden pit that drops unsuspecting victims into a lower level or pit of enemies.",
		4: "Gas Vent: Releases toxic gas into the area, causing damage over time.",
		5: "Turret Ambush: Automated turrets hidden in the environment that activate and attack when triggered.",
		6: "Falling Debris: Large chunks of debris suspended overhead that fall when disturbed.",
		7: "Poison Dart Trap: Releases poisonous darts when triggered, causing immediate damage and possible status effects.",
		8: "Spike Pit: Concealed pit filled with sharp spikes, causing damage and possibly impaling victims.",
		9: "Freeze Trap: Releases a blast of cryo energy, freezing targets in place.",
		10: "Flame Jet: Jets of flames shoot out when triggered, causing burn damage.",
		11: "Pressure Plate: Activates a trap when stepped on, triggering various effects such as explosions or releasing enemies.",
		12: "Acid Spray: Sprays acid in a cone when triggered, causing corrosive damage.",
		13: "Swinging Pendulum: A large swinging blade that slices through anything in its path.",
		14: "Teleportation Trap: Teleports victims to a random location within the area.",
		15: "Gravity Well: Creates a localized gravity anomaly, pulling victims towards it.",
		16: "Decoy Chest: Mimics a valuable loot chest but triggers a trap when opened.",
		17: "Blinding Flash: Releases a blinding flash of light, disorienting targets.",
		18: "Sonic Boom: Emits a powerful shockwave that knocks back and stuns targets.",
		19: "Magnetic Field: Disrupts electronics and metal equipment, causing malfunctions and disarming victims.",
		20: "Illusion Trap: Creates realistic illusions to deceive and confuse intruders.",
		21: "Frostbite Beam: Projects a beam of extreme cold, causing frostbite and slowing movement.",
		22: "Ethereal Snare: Conjures ethereal tendrils to restrain and immobilize victims.",
		23: "Shadow Ambush: Conceals enemies within the shadows, allowing them to ambush unsuspecting targets.",
		24: "Disintegration Field: Generates a field that disintegrates anything it touches.",
		25: "Temporal Rift: Warps time within its radius, aging or de-aging targets.",
		26: "Venomous Swarm: Unleashes a swarm of poisonous insects or creatures.",
		27: "Phase Shift Trap: Temporarily phases victims out of reality, rendering them intangible.",
		28: "Barrage Barricade: Deploys a barricade that launches projectiles at intruders.",
		29: "Blaze Wall: Creates a wall of fire that blocks passage and deals damage to those who touch it.",
		30: "Mind Control Matrix: Manipulates the minds of victims, forcing them to attack allies or perform self-harm.",
		31: "Doomsday Device: Activates a countdown to catastrophic destruction.",
		32: "Shrink Ray: Shrinks targets to miniature size, making them vulnerable and easier to defeat.",
		33: "Spectral Blade: Conjures a spectral blade that slashes through anything in its path.",
		34: "Stasis Field: Creates a field of frozen time, trapping victims within.",
		35: "Disorienting Gas: Releases a gas that causes confusion and disorientation.",
		36: "Energy Vortex: Generates a swirling vortex of energy that pulls victims towards its center.",
		37: "Chaos Sphere: Unleashes a sphere of chaotic energy that distorts reality.",
		38: "Gravitational Anomaly: Alters the gravitational pull within its radius, causing objects to float or become heavier.",
		39: "Cursed Idol: Triggers a curse upon those who touch it, bringing misfortune and calamity.",
		40: "Soul Drain: Drains the life force of victims within its radius.",
		41: "Nightmare Projection: Manifests terrifying illusions based on victims' fears.",
		42: "Time Dilation Chamber: Warps time, causing it to pass slower or faster for those within its radius.",
		43: "Inferno Pit: Creates a pit of raging fire beneath unsuspecting victims.",
		44: "Volatile Concoction: Releases a volatile chemical concoction that explodes upon contact.",
		45: "Spectral Cage: Conjures an ethereal cage that traps victims within.",
		46: "Nanobot Infestation: Releases swarms of nanobots that consume organic matter.",
		47: "Energized Floor Panels: Electrifies floor panels, shocking anyone who steps on them.",
		48: "Reality Distortion Field: Warps reality within its radius, causing disorientation and hallucinations.",
		49: "Corrupted Portal: Opens a portal to a dimension of chaos and darkness.",
		50: "Plasma Blast: Emits a powerful blast of plasma energy, incinerating anything in its path."
	}
	Trap_Manifest = []
	Traps_Count = random.randint(2, 10)  # Randomly choose the number of traps between 2 and 10
	for i in range(Traps_Count):
		random_trap_key = random.choice(list(traps.keys()))
		random_trap = traps[random_trap_key]
		Trap_Manifest.append(f"{random_trap}\n")
		
	save_to_file("Generated_Traps.txt",''.join(Trap_Manifest))
	return Trap_Manifest