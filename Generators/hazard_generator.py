import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file


def generate_random_hazard():
	hazards = {
		1: {
			"name": "Acid Pool",
			"description": "A pool of corrosive acid that burns anything that comes into contact with it.",
			"effect": "Causes severe damage over time and corrodes equipment.",
			"countermeasure": "Use protective gear or find a way to neutralize the acid."
		},
		2: {
			"name": "Explosive Barrel",
			"description": "A barrel filled with explosives, ready to detonate upon impact or proximity.",
			"effect": "Causes massive damage and knockback to anyone nearby when detonated.",
			"countermeasure": "Shoot it from a safe distance or use it strategically against enemies."
		},
		3: {
			"name": "Electric Fence",
			"description": "A fence charged with high voltage electricity, designed to deter intruders.",
			"effect": "Inflicts electric shocks and paralysis to those who touch it.",
			"countermeasure": "Disable the power source or find a way to insulate against electric shocks."
		},
		4: {
			"name": "Toxic Gas Vent",
			"description": "A vent releasing noxious gases into the air, poisoning anyone nearby.",
			"effect": "Causes poisoning, reducing health and impairing vision and movement.",
			"countermeasure": "Use a gas mask or find a way to seal off or ventilate the area."
		},
		5: {
			"name": "Falling Rocks",
			"description": "Loose rocks suspended overhead, ready to fall at any moment.",
			"effect": "Inflicts blunt force trauma and crush injuries upon impact.",
			"countermeasure": "Watch for warning signs and find cover or avoid the area entirely."
		},
		6: {
			"name": "Lava Pit",
			"description": "A pit filled with molten lava, capable of incinerating anything that falls into it.",
			"effect": "Causes instant death upon contact and deals fire damage to nearby targets.",
			"countermeasure": "Avoid stepping into the lava pit and find a safe path across."
		},
		7: {
			"name": "Poisonous Spikes",
			"description": "Sharp spikes coated with deadly poison, hidden beneath the surface.",
			"effect": "Inflicts poison status and piercing damage to those who step on them.",
			"countermeasure": "Use caution and look for signs of the spikes before moving forward."
		},
		8: {
			"name": "Quicksand",
			"description": "Loose, waterlogged sand that sucks anything that steps into it deeper and deeper.",
			"effect": "Traps victims and gradually pulls them beneath the surface, suffocating them.",
			"countermeasure": "Move slowly and avoid struggling; try to spread weight or find solid ground."
		},
		9: {
			"name": "Freezing Temperature",
			"description": "Extreme cold that can freeze exposed flesh and impair movement.",
			"effect": "Causes frostbite and hypothermia, slowing movement and reducing dexterity.",
			"countermeasure": "Wear insulated clothing and seek shelter from the cold."
		},
		10: {
			"name": "Swarm of Insects",
			"description": "A cloud of biting, stinging insects that attack anything that comes near.",
			"effect": "Inflicts poison and irritation, causing pain and distraction.",
			"countermeasure": "Use insect repellent or create a smoke screen to drive them away."
		},
		11: {
			"name": "Venomous Snakes",
			"description": "Aggressive snakes with potent venom that attack intruders on sight.",
			"effect": "Inflicts venom poisoning and paralysis with their bites.",
			"countermeasure": "Stay vigilant and use caution when traversing snake-infested areas."
		},
		12: {
			"name": "Corrosive Fumes",
			"description": "Toxic fumes released by industrial processes or chemical spills.",
			"effect": "Causes respiratory distress and corrosion to exposed surfaces.",
			"countermeasure": "Wear a gas mask and avoid prolonged exposure to the fumes."
		},
		13: {
			"name": "Blinding Light",
			"description": "Intense light that blinds and disorients those who look directly at it.",
			"effect": "Temporarily blinds and dazzles targets, impairing vision and accuracy.",
			"countermeasure": "Shield eyes or use polarized lenses to reduce the glare."
		},
		14: {
			"name": "Sonic Blast",
			"description": "A powerful shockwave of sound that knocks back and disorients nearby targets.",
			"effect": "Disorients and deafens targets, causing confusion and loss of balance.",
			"countermeasure": "Cover ears or wear noise-canceling devices to mitigate the effects."
		},
		15: {
			"name": "Magnetic Field",
			"description": "An electromagnetic field that interferes with electronics and metallic objects.",
			"effect": "Disrupts navigation systems and attracts or repels metal objects.",
			"countermeasure": "Shield electronics or use non-metallic equipment when possible."
		},
		16: {
			"name": "Radiation Leak",
			"description": "Escape of radioactive material from a containment facility or nuclear device.",
			"effect": "Causes radiation sickness and cellular damage to those exposed.",
			"countermeasure": "Wear radiation suits and minimize exposure to contaminated areas."
		},
		17: {
			"name": "Biohazardous Waste",
			"description": "Exposure to hazardous biological materials or infectious agents.",
			"effect": "Causes infection and illness, spreading disease to those exposed.",
			"countermeasure": "Handle with extreme caution and use protective gear when handling waste."
		},
		18: {
			"name": "Psychic Resonance",
			"description": "A field of psychic energy that induces hallucinations and mental instability.",
			"effect": "Causes paranoia, delusions, and violent behavior in those exposed.",
			"countermeasure": "Ground yourself and maintain mental discipline to resist the effects."
		},
		19: {
			"name": "Time Dilation",
			"description": "A temporal anomaly that distorts the flow of time, slowing or accelerating its passage.",
			"effect": "Alters perception of time, causing confusion and disorientation.",
			"countermeasure": "Focus on maintaining temporal awareness and avoid temporal anomalies."
		},
		20: {
			"name": "Gravity Anomaly",
			"description": "A localized distortion in the fabric of space-time that alters gravitational forces.",
			"effect": "Changes gravity's direction or strength, causing objects to fall or float unpredictably.",
			"countermeasure": "Adapt to changes in gravity and use caution when moving in affected areas."
		},
		21: {
			"name": "Dimensional Rift",
			"description": "A tear in the fabric of reality that leads to other dimensions or alternate realities.",
			"effect": "Creates portals or gateways to other worlds, allowing beings to pass through.",
			"countermeasure": "Close the rift or stabilize the dimensional boundary to prevent further incursions."
		},
		22: {
			"name": "Psionic Feedback",
			"description": "A backlash of psychic energy that overwhelms the minds of those nearby.",
			"effect": "Causes mental anguish and psychic trauma, rendering victims vulnerable to manipulation.",
			"countermeasure": "Shield minds or disrupt the source of psionic energy causing the feedback."
		},
		23: {
			"name": "Nano Swarm",
			"description": "A cloud of microscopic machines programmed to consume organic matter.",
			"effect": "Devours flesh and organic material, leaving behind only skeletal remains.",
			"countermeasure": "Use EMP devices or disrupt the nanites' communication to halt their activity."
		},
		24: {
			"name": "Teleportation Trap",
			"description": "A magical trap that teleports unsuspecting victims to a predetermined location.",
			"effect": "Teleports victims to a distant or dangerous location, separating them from their allies.",
			"countermeasure": "Detect and disarm the trap or find a way to counteract its teleportation effect."
		},
		25: {
			"name": "Solar Flare",
			"description": "A burst of intense radiation emitted by a nearby star, capable of incinerating anything in its path.",
			"effect": "Creates a wave of searing heat and radiation, burning exposed surfaces.",
			"countermeasure": "Seek cover or find shelter from the solar flare until it dissipates."
		},
		26: {
			"name": "Mind Control Device",
			"description": "A device that manipulates the thoughts and actions of those within its range.",
			"effect": "Overrides free will and compels victims to obey the controller's commands.",
			"countermeasure": "Disable the device or shield minds against external influence."
		},
		27: {
			"name": "Shadow Realm",
			"description": "An alternate dimension of darkness and despair, inhabited by malevolent spirits.",
			"effect": "Traps victims in an endless void of darkness, feeding on their fear and despair.",
			"countermeasure": "Find a way to pierce the veil between dimensions and escape the shadow realm."
		},
		28: {
			"name": "Soul Drain",
			"description": "A phenomenon that saps the life force from living beings, leaving them weak and frail.",
			"effect": "Drains vitality and strength, rendering victims lethargic and feeble.",
			"countermeasure": "Restore life force or shield against soul-draining effects."
		},
		29: {
			"name": "Phase Shift",
			"description": "A temporal anomaly that shifts objects and beings out of phase with reality.",
			"effect": "Phases objects in and out of existence, causing them to flicker or vanish unpredictably.",
			"countermeasure": "Stabilize phase coherence or find a way to anchor objects in reality."
		},
		30: {
			"name": "Psychic Beacon",
			"description": "A psychic resonance beacon that amplifies and broadcasts psychic energy.",
			"effect": "Enhances psychic abilities and draws psychic entities or phenomena to its location.",
			"countermeasure": "Disable the beacon or shield minds against its psychic influence."
		},
		31: {
			"name": "Nanite Infestation",
			"description": "An infestation of self-replicating nanomachines that consume and assimilate organic matter.",
			"effect": "Converts living tissue into nanites, transforming victims into mindless drones.",
			"countermeasure": "Purge nanites from the body or disrupt their communication to halt the infestation."
		},
		32: {
			"name": "Gravity Well",
			"description": "A localized distortion in gravitational forces that pulls objects toward its center.",
			"effect": "Creates a powerful gravitational field that attracts nearby objects and beings.",
			"countermeasure": "Escape the gravitational pull or find a way to counteract its effects."
		},
		33: {
			"name": "Temporal Loop",
			"description": "A repeating sequence of events trapped in a temporal anomaly, endlessly cycling through time.",
			"effect": "Traps victims in a time loop, forcing them to relive the same events over and over.",
			"countermeasure": "Break the cycle or disrupt the temporal anomaly to escape the time loop."
		},
		34: {
			"name": "Reality Distortion",
			"description": "A disruption in the fabric of reality that warps space and time.",
			"effect": "Distorts perception and alters the laws of physics within its radius.",
			"countermeasure": "Maintain mental focus and adapt to changes in reality."
		},
		35: {
			"name": "Dimensional Anomaly",
			"description": "A breach in the dimensional barrier that allows creatures from other dimensions to enter.",
			"effect": "Allows extradimensional entities to manifest in the physical world.",
			"countermeasure": "Close the dimensional rift or banish the entities back to their own realm."
		},
		36: {
			"name": "Memory Wipe",
			"description": "A psychic attack that erases memories and identity, leaving victims with amnesia.",
			"effect": "Wipes memories and personality traits, leaving victims with a blank slate.",
			"countermeasure": "Shield minds or restore memories through external stimuli."
		},
		37: {
			"name": "Time Bomb",
			"description": "An explosive device with a countdown timer set to detonate after a predetermined time.",
			"effect": "Causes massive damage and destruction upon detonation, creating a blast radius.",
			"countermeasure": "Disarm the bomb or evacuate the area before it explodes."
		},
		38: {
			"name": "Reality Collapse",
			"description": "A catastrophic event that collapses the fabric of reality, destroying everything in its path.",
			"effect": "Causes the complete breakdown of physical laws and reality itself.",
			"countermeasure": "Stabilize reality or find a way to escape to a parallel dimension."
		},
		39: {
			"name": "Death Fog",
			"description": "A poisonous fog that suffocates and kills anything that breathes it in.",
			"effect": "Causes asphyxiation and death within minutes of exposure.",
			"countermeasure": "Find a way to disperse the fog or seal off the affected area."
		},
		40: {
			"name": "Mind Warp",
			"description": "A psychic assault that distorts perception and alters consciousness.",
			"effect": "Induces hallucinations and delusions, warping reality to fit the attacker's whims.",
			"countermeasure": "Maintain mental discipline and break free from the psychic influence."
		},
		41: {
			"name": "Reality Mirror",
			"description": "A reflective surface that reflects back attacks and spells, redirecting them toward the caster.",
			"effect": "Reverses the direction of incoming attacks, causing them to harm the attacker instead.",
			"countermeasure": "Avoid direct attacks or find a way to disable or bypass the mirror."
		},
		42: {
			"name": "Dimensional Anchor",
			"description": "A device that stabilizes dimensional barriers and prevents extradimensional travel.",
			"effect": "Creates a barrier that blocks teleportation and extradimensional entities.",
			"countermeasure": "Disable the anchor or find a way to bypass its dimensional barrier."
		},
		43: {
			"name": "Quantum Entanglement",
			"description": "A phenomenon that links particles across vast distances, allowing instantaneous communication.",
			"effect": "Creates a network of interconnected particles that share information and energy.",
			"countermeasure": "Disrupt the entanglement or use it to your advantage."
		},
		44: {
			"name": "Black Hole",
			"description": "A gravitational singularity that devours matter and light, trapping anything that comes too close.",
			"effect": "Creates a gravitational well with infinite density and curvature, pulling objects inward.",
			"countermeasure": "Avoid the event horizon and find a way to escape the black hole's gravitational pull."
		},
		45: {
			"name": "Temporal Paradox",
			"description": "A contradiction or inconsistency in the timeline caused by time travel or manipulation.",
			"effect": "Creates a loop or divergence in the timeline, altering past events and future outcomes.",
			"countermeasure": "Resolve the paradox or find a way to restore the original timeline."
		},
		46: {
			"name": "Reality Erosion",
			"description": "A gradual decay of the fabric of reality, leading to the collapse of physical laws.",
			"effect": "Causes objects and beings to disintegrate or phase out of existence.",
			"countermeasure": "Stabilize reality or find a way to reinforce the fabric of spacetime."
		},
		47: {
			"name": "Entropy Cascade",
			"description": "A runaway increase in entropy that leads to the heat death of the universe.",
			"effect": "Accelerates the decay of matter and energy, leading to universal extinction.",
			"countermeasure": "Reverse the entropy cascade or find a way to escape its effects."
		},
		48: {
			"name": "Reality Shatter",
			"description": "A sudden rupture in the fabric of reality, causing nearby objects to fragment and dissolve.",
			"effect": "Shatters reality into fragments, creating rifts and distortions in spacetime.",
			"countermeasure": "Stabilize the shattered reality or find a way to escape its effects."
		},
		49: {
			"name": "Chrono Distortion",
			"description": "A disruption in the flow of time that warps perception and alters causality.",
			"effect": "Creates temporal anomalies and paradoxes, changing past events and future outcomes.",
			"countermeasure": "Restore temporal stability or find a way to navigate the distortions in time."
		},
		50: {
			"name": "Reality Warp",
			"description": "A manipulation of reality that alters the laws of physics and bends spacetime to the user's will.",
			"effect": "Twists reality to fit the user's desires, reshaping the world according to their whims.",
			"countermeasure": "Break the user's concentration or find a way to counteract their reality-warping powers."
		}
	}
	hazard_manifest = []
	hazards_Count = random.randint(2, 10)  # Randomly choose the number of puzzles between 2 and 10
	for i in range(hazards_Count):
		random_hazardse_key = random.choice(list(hazards.keys()))
		random_hazards = hazards[random_hazardse_key]
		# Append name, description, effect, and a counter measure
		hazard_manifest.append(f"name: {random_hazards['name']}")
		hazard_manifest.append(f"Description: {random_hazards['description']}")
		hazard_manifest.append(f"effect: {random_hazards['effect']}")
		hazard_manifest.append(f"countermeasure: {random_hazards['countermeasure']}\n")

	with open("Generated_hazards.txt", "w") as file:
		for item in hazard_manifest:
			file.write(f"{item}\n")

	return hazard_manifest