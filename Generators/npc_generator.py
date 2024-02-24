import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file


def generate_random_npc():
	# Dictionary of NPC occupations
	occupations = {
		"Vault Hunter": "Brave adventurers who seek out Vaults and the treasures within.",
		"Bandit": "Lawless marauders who pillage and plunder across the wastelands.",
		"Crimson Raider": "Members of the resistance group fighting against the tyrannical forces of Handsome Jack.",
		"Mercenary": "Hired guns willing to do anything for the right price.",
		"Gunslinger": "Quick-drawing sharpshooters with deadly accuracy.",
		"Bounty Hunter": "Trackers and killers hired to hunt down dangerous targets.",
		"Mechanic": "Skilled technicians who specialize in repairing and modifying vehicles and machinery.",
		"Engineer": "Inventive minds adept at building and maintaining complex systems.",
		"Sellsword": "Mercenaries who offer their services to the highest bidder.",
		"Nomad": "Wandering warriors who roam the lands in search of adventure and fortune.",
		"Tinkerer": "Craftsmen who excel at tinkering with gadgets and devices.",
		"Scavenger": "Resourceful survivors who scavenge and salvage whatever they can find.",
		"Outlaw": "Outcasts and rebels who defy authority and live by their own rules.",
		"Gladiator": "Skilled fighters who thrive in arenas and combat arenas.",
		"Scooter's Catch-a-Ride Operator": "Operators of vehicle stations providing transportation across Pandora.",
		"Techie": "Tech-savvy individuals who excel at hacking and digital manipulation.",
		"Medic": "Healers who provide medical aid and support to allies in need.",
		"Gadgeteer": "Inventors and creators of innovative gadgets and gizmos.",
		"Slaughterer": "Bloodthirsty warriors who revel in the chaos and carnage of battle.",
		"Pandoran Wildlife Expert": "Experts in the study and management of the dangerous creatures of Pandora.",
		"Smuggler": "Underground traders who specialize in smuggling contraband and illicit goods.",
		"Brick's Bouncer": "Enforcers and bodyguards employed by the fearsome Brick.",
		"Dahl Soldier": "Soldiers and mercenaries employed by the Dahl Corporation.",
		"Hyperion Engineer": "Engineers and technicians working for the powerful Hyperion Corporation.",
		"Jakobs Gunslinger": "Deadly marksmen armed with Jakobs firearms known for their high damage and accuracy.",
		"Maliwan Scientist": "Scientists and researchers employed by the Maliwan Corporation to develop advanced weaponry.",
		"Torgue Demolitionist": "Experts in explosives and heavy weaponry employed by the Torgue Corporation.",
		"Vladof Revolutionary": "Revolutionaries and freedom fighters fighting against corporate oppression.",
		"Atlas Surveyor": "Explorers and cartographers mapping uncharted territories for the Atlas Corporation.",
		"Eridium Miner": "Miners who extract the valuable mineral Eridium from Pandora's surface.",
		"Tediore Technician": "Technicians responsible for the production and maintenance of Tediore firearms.",
		"Anshin Field Medic": "Medics and healers employed by Anshin Corporation to provide medical aid in combat zones.",
		"Dahl Mercenary": "Mercenaries hired by the Dahl Corporation to enforce their corporate interests.",
		"Jakobs Huntsman": "Skilled hunters and trackers employed by the Jakobs Corporation.",
		"Maliwan Researcher": "Researchers and scientists working for the Maliwan Corporation to develop cutting-edge technology.",
		"Torgue Enforcer": "Enforcers and heavy weapons specialists employed by the Torgue Corporation.",
		"Vladof Guerrilla": "Guerilla fighters and insurgents fighting against corporate dominance.",
		"Atlas Cartographer": "Cartographers and explorers mapping Pandora's dangerous terrain for the Atlas Corporation."
	}



	# Dictionary of NPC quirks
	quirks = [
		"Always wears a bandana over their face.",
		"Has a cybernetic arm.",
		"Speaks in rhyme.",
		"Is terrified of heights.",
		"Carries a lucky charm at all times.",
		"Never removes their helmet.",
		"Has an unusual pet.",
		"Collects rare artifacts.",
		"Is obsessed with explosions.",
		"Has a mysterious past.",
		"Constantly chews on toothpicks.",
		"Wears mismatched socks.",
		"Has an irrational fear of robots.",
		"Always carries a deck of playing cards.",
		"Speaks with a fake accent.",
		"Is a hopeless romantic.",
		"Never sleeps.",
		"Has a penchant for collecting hats.",
		"Is allergic to everything.",
		"Is haunted by their past.",
		"Has a strange fascination with insects.",
		"Believes they have psychic powers.",
		"Hates the color green.",
		"Can't stand the sound of ticking clocks.",
		"Is an amateur inventor.",
		"Believes they are cursed.",
		"Claims to have seen a UFO.",
		"Has an imaginary friend.",
		"Talks to themselves.",
		"Believes they are a reincarnated ancient warrior.",
		"Is convinced they are being followed by spies.",
		"Has a fear of open spaces.",
		"Always carries a journal and writes down everything.",
		"Is a conspiracy theorist.",
		"Has a collection of rare coins.",
		"Claims to have traveled through time.",
		"Can't stand the taste of chocolate.",
		"Believes in ghosts.",
		"Has an extreme fear of germs.",
		"Is a compulsive liar.",
		"Has a knack for getting lost.",
		"Is afraid of the dark.",
		"Has a fear of clowns.",
		"Is a hoarder.",
		"Has a fear of water.",
		"Is an adrenaline junkie.",
		"Has a secret talent for singing.",
		"Believes they are being watched by aliens.",
		"Has a fascination with the occult.",
		"Can't stand the smell of flowers."
	]

	def generate_npc():
		name = generate_name()
		occupation = random.choice(list(occupations.keys()))
		description = occupations[occupation]
		quirk = random.choice(quirks)
		
		npc = {
			"Name": name,
			"Occupation": occupation,
			"Description": description,
			"Quirk": quirk,
		}
		
		return npc

	def generate_name():
		# List of first names
		first_names = [
			"Axelia", "Cyrus", "Rhea", "Helios", "Nova", "Terra", "Orion", "Zephyr", "Titan", "Aria",
			"Nyx", "Vega", "Triton", "Astrid", "Phoenix", "Echo", "Luna", "Atlas", "Sirius", "Nebula",
			"Apollo", "Gaia", "Celeste", "Zenith", "Pandora", "Siren", "Titan", "Hyperion", "Reaper",
			"Moxxi", "Athena", "Morpheus", "Electra", "Orion", "Perseus", "Artemis", "Hera", "Hades",
			"Hermes", "Demeter", "Dionysus", "Hermes", "Hestia", "Eos", "Selene", "Helios", "Eris",
			"Janus", "Chaos", "Hypnos"
		]

		# List of last names
		last_names = [
			"Ironside", "Darkstar", "Blackthorn", "Nightshade", "Shadowstrike", "Stormrage", "Frostbane",
			"Firestorm", "Grimlock", "Silvermoon", "Steelheart", "Bloodmoon", "Thunderclap", "Shadowcaster",
			"Goldfire", "Stonebreaker", "Doomhammer", "Thornblade", "Ashborn", "Blackstone", "Moonshadow",
			"Frostfang", "Grimfist", "Ironblood", "Nightwalker", "Shadowborn", "Stormbreaker", "Thunderstrike",
			"Winterborn", "Fireheart", "Emberblade", "Nightshade", "Frostwind", "Shadowcaster", "Thunderfist",
			"Emberheart", "Ironclaw", "Stormbringer", "Fireforge", "Nightstalker", "Frostbite", "Shadowhunter",
			"Thunderstorm", "Emberflare", "Ironhelm", "Stormshield", "Firebrand", "Nightfall", "Frostfire",
			"Shadowblade"
		]
				
		# Generate a random name
		first_name = random.choice(first_names)
		last_name = random.choice(last_names)
		full_name = f"{first_name} {last_name}"
		
		return full_name

	# Generate NPCs
	npcs = [generate_npc() for _ in range(50)]

	# Write NPCs to file
	with open("npcs.txt", "w") as file:
		for npc in npcs:
			file.write(f"Name: {npc['Name']}\n")
			file.write(f"Occupation: {npc['Occupation']}\n")
			file.write(f"Description: {npc['Description']}\n")
			file.write(f"Quirk: {npc['Quirk']}\n")
			file.write("\n")  # Add a blank line between NPCs
	return npcs