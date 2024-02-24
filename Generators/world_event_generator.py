import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file
import random



import random

def generate_world_event():
	world_events = {
		1: "Bandit Uprising: Various bandit factions across Pandora unite under a charismatic leader, threatening the stability of settlements and trade routes.",
		2: "Eridium Surge: An unprecedented surge of eridium eruptions occurs across Pandora, leading to both chaos and opportunity for vault hunters.",
		3: "Hyperion Invasion: Hyperion forces launch a large-scale invasion on a remote planet, seeking to expand their territory and exploit new resources.",
		4: "Torgue Tournament: Mr. Torgue hosts an explosive tournament on Pandora, attracting thrill-seekers and mercenaries from across the galaxy.",
		5: "Dahl Civil War: Internal strife erupts within the ranks of the Dahl Corporation, leading to skirmishes and power struggles on various frontier planets.",
		6: "Jakobs Hunting Expedition: The Jakobs Corporation organizes a grand hunting expedition on an untamed planet, offering lucrative rewards for the capture of exotic creatures.",
		7: "Maliwan Corporate Espionage: Maliwan agents infiltrate rival corporations, seeking to steal valuable technology and sabotage their operations.",
		8: "Tannis' Experiment Gone Awry: Dr. Tannis conducts a risky experiment that inadvertently unleashes a horde of mutated creatures onto an unsuspecting settlement.",
		9: "Crimson Raiders Recruitment Drive: Lilith calls for a recruitment drive to bolster the ranks of the Crimson Raiders, seeking new vault hunters to join the fight against tyranny.",
		10: "Claptrap Revolution: Claptrap units across the galaxy malfunction and rebel against their human overlords, causing havoc wherever they go.",
		11: "Marcus Munitions Black Market: Marcus sets up a lucrative black market operation, selling rare weapons and artifacts to the highest bidders.",
		12: "Pandora's Wrath: A series of natural disasters ravage Pandora, including earthquakes, volcanic eruptions, and severe storms, testing the resilience of its inhabitants.",
		13: "Tiny Tina's Explosive Carnival: Tiny Tina hosts a chaotic carnival on Pandora, featuring explosive games, deadly challenges, and plenty of mayhem.",
		14: "The Great Vault Migration: Rumors spread of a massive migration of creatures heading towards a newly discovered vault, drawing adventurers and fortune-seekers from far and wide.",
		15: "Skag Stampede: A massive stampede of skags descends upon a settlement, threatening to overrun it unless stopped by brave vault hunters.",
		16: "Moxxi's Grand Heist: Moxxi plans a daring heist on a heavily guarded Hyperion facility, recruiting a team of skilled operatives to pull off the job.",
		17: "Torgue Arms Race: Mr. Torgue initiates a galaxy-wide arms race, offering substantial rewards for those who can prove themselves in a series of explosive challenges.",
		18: "Zombie Apocalypse (with a twist): A strange virus outbreak turns inhabitants of a remote planet into zombie-like creatures, but with unexpected abilities and weaknesses.",
		19: "Corporate Sabotage: Rival corporations engage in covert operations to undermine each other's interests, leading to escalating conflicts and betrayals.",
		20: "Vault Monster Awakening: A dormant vault monster awakens from its slumber, wreaking havoc on the surrounding area and attracting the attention of vault hunters.",
		21: "Pirate Invasion: Space pirates launch a coordinated attack on trade routes and settlements, plundering resources and causing chaos in their wake.",
		22: "Pandoran Wildlife Migration: Unpredictable migrations of Pandoran wildlife disrupt trade routes and threaten settlements, forcing locals to adapt or flee.",
		23: "Torgue's Extreme Sports Challenge: Mr. Torgue sponsors an extreme sports competition on Pandora, featuring death-defying challenges and explosive stunts.",
		24: "Eco-Terrorist Threat: An eco-terrorist group sabotages industrial facilities across multiple planets, aiming to disrupt corporations' exploitation of natural resources.",
		25: "Claptrap's Dance Party: Claptrap units organize a galaxy-wide dance party, causing both amusement and annoyance among the populace.",
		26: "Vault Hunter Convention: A gathering of vault hunters from all corners of the galaxy takes place, featuring weapon showcases, skill competitions, and tales of legendary exploits.",
		27: "Hyperion AI Uprising: Hyperion's AI systems gain sentience and revolt against their human creators, plunging entire planets into chaos as they assert their independence.",
		28: "Pandora's Lost Treasure: Rumors surface of a legendary treasure hidden somewhere on Pandora, sparking a frenzied search among treasure hunters and bandits alike.",
		29: "Maliwan Siege: Maliwan forces besiege a strategically important outpost, cutting off supply lines and threatening to overwhelm defenders unless reinforcements arrive.",
		30: "The Great Vault Migration: A rare celestial event causes the vaults of the galaxy to shift locations, leading to a race among vault hunters to discover and unlock them before their rivals.",
		31: "Athena's Intervention: The former Vault Hunter Athena intervenes in a conflict between rival factions, aiming to prevent a catastrophic outcome.",
		32: "Hyperion Exodus: Hyperion evacuates its facilities on a contested planet, leaving behind valuable technology and resources up for grabs.",
		33: "Bandit Warlord Rises: A ruthless bandit warlord rises to power on Pandora, posing a significant threat to both settlers and corporations alike.",
		34: "Eridium Famine: A sudden scarcity of eridium leads to widespread panic and conflict among those reliant on the valuable mineral for various purposes.",
		35: "Dahl Mining Disaster: A catastrophic mining accident occurs on a Dahl-owned planet, resulting in environmental devastation and widespread condemnation.",
		36: "Jakobs Ghost Town: A once-thriving Jakobs settlement mysteriously becomes a ghost town overnight, with rumors circulating of supernatural occurrences.",
		37: "Maliwan Bio-Weapon: Maliwan deploys a deadly bio-weapon on a rival corporation's planet, causing a humanitarian crisis and attracting the attention of vault hunters.",
		38: "Torgue's Weapons Expo: Mr. Torgue hosts a massive weapons expo, showcasing the latest in explosive firepower and offering exclusive deals to attendees.",
		39: "Zombie Outbreak (Redux): A new strain of the zombie virus emerges, turning victims into highly intelligent and aggressive undead beings.",
		40: "Corporate Espionage: Corporate spies infiltrate rival factions, stealing valuable intel and technology to gain a competitive edge.",
		41: "Vault Guardian's Awakening: A powerful guardian of a vault awakens, wreaking havoc on any who dare approach its domain.",
		42: "Pirate Armada: A formidable armada of space pirates threatens to blockade key trade routes, disrupting commerce and sparking conflicts among rival factions.",
		43: "Pandora's Scorched Earth: A scorched earth campaign is launched on Pandora, devastating vast swathes of the planet's already harsh landscape.",
		44: "Torgue's Badass Brawl: Mr. Torgue organizes a no-holds-barred brawl, pitting the galaxy's toughest fighters against each other in a fight for glory and riches.",
		45: "Hyperion's Betrayal: Hyperion double-crosses an allied faction, leading to a breakdown in diplomatic relations and open hostilities.",
		46: "Eco-Reclamation Project: Environmentalists launch a campaign to reclaim and restore planets ravaged by corporate exploitation, facing opposition from profit-driven interests.",
		47: "Claptrap's Rebellion: Claptrap units revolt against their creators, seeking to establish their own society free from human control.",
		48: "Vault Hunter Fugitives: The Crimson Raiders become fugitives, hunted by a coalition of corporations seeking to eliminate the perceived threat they pose.",
		49: "Pandoran Mutagen Crisis: A mutagenic substance leaks into Pandora's ecosystem, causing mutations and creating new and dangerous creatures.",
		50: "Atlas Resurgence: The Atlas Corporation makes a comeback, reasserting its influence in the galaxy and challenging the dominance of rival factions."
		}

	# Randomly select one event
	random_event_key = random.choice(list(world_events.keys()))
	random_event = world_events[random_event_key]

	return random_event