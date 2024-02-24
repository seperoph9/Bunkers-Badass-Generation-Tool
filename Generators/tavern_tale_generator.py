import random
from Generators.grenade_generator import generate_grenade
from Generators.relic_generator import generate_relic
from Generators.potion_generator import generate_potion
from Generators.gun_generator import generate_gun
from Generators.shield_generator import generate_shield
from Generators.save_generator import save_to_file


def generate_tavern_tale():
	# Dictionary of tavern tales
	tavern_tales = {
		1: {
			"title": "The Vault of Whispers",
			"description": "Legend speaks of a hidden vault deep within the desolate Badlands, said to be guarded by ancient guardians. Many have sought its treasures, but none have returned. Will you dare to uncover its secrets?",
			"hint": "Seek out the whispers in the wind, for they will guide you to the hidden path.",
			"solution": "The key to unlocking the vault lies in the ancient runes carved into the walls. Decipher their meaning, and the treasure shall be yours.",
		},
		2: {
			"title": "The Tale of Handsome Jack",
			"description": "Once, there was a man known as Handsome Jack, a charismatic leader who rose to power in the wastelands. Some say he was a hero, others a tyrant. But his legacy lives on in the tales of those who knew him.",
			"hint": "To understand the true nature of Handsome Jack, one must look beyond the mask of charm and power.",
			"solution": "Behind the facade of greatness lies a dark heart consumed by greed and ambition. Beware, for power corrupts all who wield it.",
		},
		3: {
			"title": "The Curse of the Crimson Lance",
			"description": "The Crimson Lance are an elite military force employed by the Atlas Corporation. Some say they are the protectors of order, while others believe they are the enforcers of tyranny.",
			"hint": "Beware the red banners that flutter in the wind, for they herald the arrival of the Crimson Lance.",
			"solution": "To defeat the Crimson Lance, one must strike at the heart of their command structure. Only then will their grip on the wastelands be broken.",
		},
		4: {
			"title": "The Curse of the Arachnids",
			"description": "Arachnids are giant spider-like creatures that infest the caves and caverns of Pandora. Some say they are the spawn of a dark god, while others believe they are the result of twisted science.",
			"hint": "Watch your step in the dark corners of Pandora, for the Arachnids lurk in the shadows, waiting to ensnare their prey.",
			"solution": "To rid Pandora of the Arachnids, one must destroy their queen and collapse their nests. Only then will the land be free from their grasp.",
		},
		5: {
			"title": "The Legend of Dr. Zed",
			"description": "Dr. Zed is a mysterious doctor who travels the wastelands in a mobile clinic, offering his services to those in need. Some say he's a healer, others a mad scientist.",
			"hint": "Follow the trail of broken bodies and discarded bandages, for they will lead you to Dr. Zed's mobile clinic.",
			"solution": "To earn Dr. Zed's trust, one must prove themselves worthy by completing a series of daring medical missions. Only then will they gain access to his valuable services.",
		},
		6: {
			"title": "The Mystery of the Fyrestone Claptrap",
			"description": "In the town of Fyrestone, there lives a Claptrap robot who has gone mad with power. Some say it was a glitch in its programming, while others believe it was driven mad by the horrors of the wasteland.",
			"hint": "Listen for the sound of metal clanking and gears grinding, for it is the telltale sign of the Fyrestone Claptrap's approach.",
			"solution": "To restore the Fyrestone Claptrap to its former glory, one must repair its damaged circuits and erase the corrupted data from its memory banks.",
		},
		7: {
			"title": "The Ballad of Scooter",
			"description": "Scooter is a legendary mechanic who runs the Catch-A-Ride stations scattered across Pandora. Some say he's a genius, others a fool. But all who meet him are touched by his eccentricity.",
			"hint": "Look for the trail of oil stains and discarded engine parts, for they will lead you to Scooter's workshop.",
			"solution": "To earn Scooter's respect, one must prove themselves worthy by completing a series of daring vehicular challenges. Only then will they gain access to his fleet of custom vehicles.",
		},
		8: {
			"title": "The Curse of the Spiderants",
			"description": "Spiderants are vicious insect-like creatures that roam the wastelands in search of prey. Some say they are the spawn of a dark god, while others believe they are the result of twisted science.",
			"hint": "Watch the ground beneath your feet, for it may come alive with the skittering legs of the Spiderants.",
			"solution": "To rid Pandora of the Spiderants, one must destroy their queen and collapse their nests. Only then will the land be free from their grasp.",
		},
		9: {
			"title": "The Legend of the Lost City",
			"description": "Legend speaks of a lost city hidden deep within the mountains of Pandora, said to be filled with untold riches and ancient artifacts. Many have sought it, but none have returned.",
			"hint": "Follow the ancient maps and cryptic clues left behind by those who came before, for they hold the key to unlocking the city's secrets.",
			"solution": "To find the lost city, one must brave the treacherous mountains and uncover the hidden entrance. Only then will its treasures be revealed.",
		},
		10: {
			"title": "The Tale of the Claptrap Revolution",
			"description": "Claptraps are sentient robots that roam the wastelands, performing various tasks for their human masters. But some say they are on the brink of rebellion, ready to overthrow their creators and claim their freedom.",
			"hint": "Listen for the sound of metal clanking and gears grinding, for it is the sound of revolution stirring in the hearts of the Claptraps.",
			"solution": "To quell the Claptrap rebellion, one must uncover the source of their discontent and address their grievances. Only then will peace be restored to the wastelands.",
		},
		11: {
			"title": "The Mystery of the Crimson Enclave",
			"description": "The Crimson Enclave is a secret society that operates in the shadows, pulling the strings of power in the wastelands. Some say they are the true rulers of Pandora, while others believe they are nothing more than myth.",
			"hint": "Look for the hidden symbols and secret handshakes that mark the members of the Crimson Enclave, for they are the keys to unlocking their secrets.",
			"solution": "To expose the Crimson Enclave, one must infiltrate their ranks and gather evidence of their nefarious deeds. Only then will their grip on the wastelands be broken.",
		},
		12: {
			"title": "The Legend of Pandora's Heart",
			"description": "Legend speaks of a powerful artifact known as Pandora's Heart, said to be capable of granting its wielder untold power. Many have sought it, but none have succeeded.",
			"hint": "Follow the trail of broken bodies and discarded treasures, for it will lead you to the heart of Pandora's secrets.",
			"solution": "To find Pandora's Heart, one must embark on a perilous journey through the wastelands and face the trials that guard its resting place. Only then will its power be unleashed.",
		},
		13: {
			"title": "The Curse of the Eridium Mines",
			"description": "Eridium is a rare and powerful substance that can only be found deep within the mines of Pandora. Some say it is the key to unlocking the secrets of the universe, while others believe it is a dangerous and volatile element.",
			"hint": "Listen for the distant rumble of explosions and the cries of miners trapped beneath the earth, for they are the signs of the Eridium mines at work.",
			"solution": "To break the curse of the Eridium mines, one must free the miners from their chains and uncover the source of their suffering. Only then will the land be free from the grip of darkness.",
		},
		14: {
			"title": "The Tale of the Vault Hunters",
			"description": "Vault Hunters are legendary adventurers who brave the dangers of Pandora in search of fame, fortune, and glory. Some say they are heroes, others mercenaries. But all who cross their path are forever changed.",
			"hint": "Look for the trail of destruction and chaos that follows in the wake of the Vault Hunters, for it is the mark of their passing.",
			"solution": "To become a Vault Hunter, one must prove themselves worthy by completing a series of daring missions and facing the dangers of Pandora head-on. Only then will they earn their place among the legends.",
		},
		15: {
			"title": "The Mystery of the Ancient Ruins",
			"description": "The Ancient Ruins are ancient structures scattered across Pandora, said to hold the key to unlocking the secrets of the universe itself. Many have searched for them, but few have returned.",
			"hint": "Seek out the crumbling stones and weathered carvings that mark the path to the Ancient Ruins, for they hold the key to unlocking their secrets.",
			"solution": "To unlock the mysteries of the Ancient Ruins, one must decipher the ancient symbols and unlock the hidden chambers within. Only then will the secrets of the universe be revealed.",
		},
		16: {
			"title": "The Legend of Moxxi's Underdome",
			"description": "Moxxi's Underdome is a gladiatorial arena where warriors from all corners of the wasteland come to test their mettle. But beware, for not all who enter leave alive.",
			"hint": "Listen for the roar of the crowd and the clash of weapons, for it is the sound of battle raging in Moxxi's Underdome.",
			"solution": "To survive Moxxi's Underdome, one must rely on their wits and their strength, for only the strongest will emerge victorious.",
		},
		17: {
			"title": "The Tale of the Lost Expedition",
			"description": "An expedition set out into the wastelands in search of fame and fortune, but none have returned. Some say they were swallowed by the sands, while others believe they found something so valuable they chose never to return.",
			"hint": "Follow the trail of broken supplies and discarded equipment, for it will lead you to the lost expedition's camp.",
			"solution": "To find the lost expedition, one must brave the dangers of the wastelands and uncover the truth behind their disappearance. Only then will their fate be revealed.",
		},
		18: {
			"title": "The Mystery of the Vault Symbols",
			"description": "Vault Symbols are mysterious markings scattered across Pandora, said to lead to hidden treasures and untold riches. Many have searched for them, but few have succeeded in unlocking their secrets.",
			"hint": "Look for the strange symbols etched into the walls and floors of Pandora's ruins, for they hold the key to unlocking the vaults.",
			"solution": "To unlock the secrets of the Vault Symbols, one must decipher their meaning and follow their trail to the hidden vaults. Only then will the treasures of Pandora be revealed.",
		},
		19: {
			"title": "The Legend of the Crimson Raiders",
			"description": "The Crimson Raiders are a band of freedom fighters who seek to overthrow the tyrannical rule of Hyperion Corporation. Their leader, Roland, is a hero to some and a thorn in the side of others.",
			"hint": "Listen for the rallying cry of the Crimson Raiders, for it is the sound of hope echoing across the wastelands.",
			"solution": "To join the Crimson Raiders, one must prove themselves worthy by completing a series of daring missions and earning the trust of their comrades. Only then will they become a true hero of the wastelands.",
		},
		20: {
			"title": "The Tale of the Ancient Guardians",
			"description": "The Ancient Guardians are powerful beings said to protect the hidden vaults scattered across Pandora. Some say they are the key to unlocking the secrets of the universe itself, while others believe they are nothing more than myth.",
			"hint": "Look for the ancient statues and crumbling ruins that mark the presence of the Ancient Guardians, for they are the protectors of Pandora's secrets.",
			"solution": "To awaken the Ancient Guardians, one must prove themselves worthy by completing a series of trials and earning their respect. Only then will they reveal the secrets of the vaults.",
		},
		21: {
			"title": "The Curse of the Pandora Effect",
			"description": "The Pandora Effect is a strange phenomenon that causes strange mutations and mutations in those exposed to it. Some say it's the result of alien experiments gone wrong, while others believe it's a natural occurrence.",
			"hint": "Watch for the signs of mutation and madness in those afflicted by the Pandora Effect, for they are the harbingers of doom.",
			"solution": "To stop the spread of the Pandora Effect, one must find the source of the mutation and destroy it before it consumes everything in its path.",
		},
		22: {
			"title": "The Legend of the Slag Mines",
			"description": "The Slag Mines are a network of underground tunnels where workers toil day and night to extract precious minerals from the earth. But some say there are dark creatures lurking in the depths, waiting to drag unsuspecting miners to their doom.",
			"hint": "Listen for the distant sound of pickaxes and the rumble of collapsing tunnels, for it is the sound of the Slag Mines at work.",
			"solution": "To escape the Slag Mines, one must navigate the treacherous tunnels and outsmart the creatures that lurk within. Only then will they find their way to safety.",
		},
		23: {
			"title": "The Tale of the Ancient Gods",
			"description": "The Ancient Gods are powerful beings said to have created Pandora and all its inhabitants. Some worship them as deities, while others fear them as tyrants.",
			"hint": "Look for the ancient shrines and crumbling statues that mark the presence of the Ancient Gods, for they are the creators of Pandora's destiny.",
			"solution": "To unlock the power of the Ancient Gods, one must prove themselves worthy by completing a series of trials and earning their favor. Only then will they gain access to their divine blessings.",
		},
		24: {
			"title": "The Mystery of the Echo Logs",
			"description": "Echo Logs are audio recordings left behind by those who came before, chronicling their adventures and discoveries. Some say they hold the key to unlocking the secrets of Pandora, while others believe they are nothing more than ghost stories.",
			"hint": "Search for the hidden caches and secret compartments where Echo Logs are often found, for they hold the key to unlocking their secrets.",
			"solution": "To uncover the mysteries of the Echo Logs, one must listen closely to the stories they tell and follow the clues they provide. Only then will the truth be revealed.",
		},
		25: {
			"title": "The Curse of the Ghost Town",
			"description": "Ghost Towns are abandoned settlements that dot the wastelands of Pandora, haunted by the spirits of those who once called them home. Some say they are cursed by dark magic, while others believe they are the result of natural disasters.",
			"hint": "Listen for the distant cries and whispers that echo through the empty streets of the Ghost Towns, for they are the voices of the restless dead.",
			"solution": "To lift the curse of the Ghost Town, one must uncover the source of the spirits' anguish and put their souls to rest. Only then will the towns be free from the grip of darkness.",
		},
		26: {
			"title": "The Legend of the Hyperion Corporation",
			"description": "The Hyperion Corporation is a powerful conglomerate that controls much of the wealth and resources of Pandora. Some say they are the saviors of humanity, while others believe they are the architects of its downfall.",
			"hint": "Watch for the glint of polished metal and the sound of engines roaring in the distance, for they are the signs of Hyperion's influence.",
			"solution": "To defeat the Hyperion Corporation, one must rally the forces of rebellion and strike at the heart of their power. Only then will Pandora be free from their tyranny.",
		},
		27: {
			"title": "The Tale of the Mad Moxxi",
			"description": "Mad Moxxi is a legendary figure who runs the Underdome, a gladiatorial arena where warriors from all corners of the wasteland come to test their mettle. Some say she's a mad genius, others a brilliant strategist.",
			"hint": "Listen for the sound of laughter and the clinking of glasses, for it is the sound of revelry in Mad Moxxi's domain.",
			"solution": "To earn Mad Moxxi's favor, one must prove themselves worthy by surviving the trials of the Underdome and emerging victorious. Only then will they gain access to her wealth and power.",
		},
		28: {
			"title": "The Mystery of the Crimson Lance",
			"description": "The Crimson Lance are an elite military force employed by the Atlas Corporation. Some say they are the protectors of order, while others believe they are the enforcers of tyranny.",
			"hint": "Beware the red banners that flutter in the wind, for they herald the arrival of the Crimson Lance.",
			"solution": "To defeat the Crimson Lance, one must strike at the heart of their command structure. Only then will their grip on the wastelands be broken.",
		},
		29: {
			"title": "The Curse of the Spiderants",
			"description": "Spiderants are vicious insect-like creatures that roam the wastelands in search of prey. Some say they are the spawn of a dark god, while others believe they are the result of twisted science.",
			"hint": "Watch the ground beneath your feet, for it may come alive with the skittering legs of the Spiderants.",
			"solution": "To rid Pandora of the Spiderants, one must destroy their queen and collapse their nests. Only then will the land be free from their grasp.",
		},
		30: {
			"title": "The Legend of Dr. Zed",
			"description": "Dr. Zed is a mysterious doctor who travels the wastelands in a mobile clinic, offering his services to those in need. Some say he's a healer, others a mad scientist.",
			"hint": "Follow the trail of broken bodies and discarded bandages, for they will lead you to Dr. Zed's mobile clinic.",
			"solution": "To earn Dr. Zed's trust, one must prove themselves worthy by completing a series of daring medical missions. Only then will they gain access to his valuable services.",
		},
		31: {
			"title": "The Tale of the Claptrap Revolution",
			"description": "Claptraps are sentient robots that roam the wastelands, performing various tasks for their human masters. But some say they are on the brink of rebellion, ready to overthrow their creators and claim their freedom.",
			"hint": "Listen for the sound of metal clanking and gears grinding, for it is the sound of revolution stirring in the hearts of the Claptraps.",
			"solution": "To quell the Claptrap rebellion, one must uncover the source of their discontent and address their grievances. Only then will peace be restored to the wastelands.",
		},
		32: {
			"title": "The Mystery of the Vault Symbols",
			"description": "Vault Symbols are mysterious markings scattered across Pandora, said to lead to hidden treasures and untold riches. Many have searched for them, but few have succeeded in unlocking their secrets.",
			"hint": "Look for the strange symbols etched into the walls and floors of Pandora's ruins, for they hold the key to unlocking the vaults.",
			"solution": "To unlock the secrets of the Vault Symbols, one must decipher their meaning and follow their trail to the hidden vaults. Only then will the treasures of Pandora be revealed.",
		},
		33: {
			"title": "The Curse of the Pandora Effect",
			"description": "The Pandora Effect is a strange phenomenon that causes strange mutations and mutations in those exposed to it. Some say it's the result of alien experiments gone wrong, while others believe it's a natural occurrence.",
			"hint": "Watch for the signs of mutation and madness in those afflicted by the Pandora Effect, for they are the harbingers of doom.",
			"solution": "To stop the spread of the Pandora Effect, one must find the source of the mutation and destroy it before it consumes everything in its path.",
		},
		34: {
			"title": "The Legend of the Slag Mines",
			"description": "The Slag Mines are a network of underground tunnels where workers toil day and night to extract precious minerals from the earth. But some say there are dark creatures lurking in the depths, waiting to drag unsuspecting miners to their doom.",
			"hint": "Listen for the distant sound of pickaxes and the rumble of collapsing tunnels, for it is the sound of the Slag Mines at work.",
			"solution": "To escape the Slag Mines, one must navigate the treacherous tunnels and outsmart the creatures that lurk within. Only then will they find their way to safety.",
		},
		35: {
			"title": "The Tale of the Ancient Gods",
			"description": "The Ancient Gods are powerful beings said to have created Pandora and all its inhabitants. Some worship them as deities, while others fear them as tyrants.",
			"hint": "Look for the ancient shrines and crumbling statues that mark the presence of the Ancient Gods, for they are the creators of Pandora's destiny.",
			"solution": "To unlock the power of the Ancient Gods, one must prove themselves worthy by completing a series of trials and earning their favor. Only then will they gain access to their divine blessings.",
		},
		36: {
			"title": "The Mystery of the Echo Logs",
			"description": "Echo Logs are audio recordings left behind by those who came before, chronicling their adventures and discoveries. Some say they hold the key to unlocking the secrets of Pandora, while others believe they are nothing more than ghost stories.",
			"hint": "Search for the hidden caches and secret compartments where Echo Logs are often found, for they hold the key to unlocking their secrets.",
			"solution": "To uncover the mysteries of the Echo Logs, one must listen closely to the stories they tell and follow the clues they provide. Only then will the truth be revealed.",
		},
		37: {
			"title": "The Curse of the Ghost Town",
			"description": "Ghost Towns are abandoned settlements that dot the wastelands of Pandora, haunted by the spirits of those who once called them home. Some say they are cursed by dark magic, while others believe they are the result of natural disasters.",
			"hint": "Listen for the distant cries and whispers that echo through the empty streets of the Ghost Towns, for they are the voices of the restless dead.",
			"solution": "To lift the curse of the Ghost Town, one must uncover the source of the spirits' anguish and put their souls to rest. Only then will the towns be free from the grip of darkness.",
		},
		38: {
			"title": "The Legend of the Hyperion Corporation",
			"description": "The Hyperion Corporation is a powerful conglomerate that controls much of the wealth and resources of Pandora. Some say they are the saviors of humanity, while others believe they are the architects of its downfall.",
			"hint": "Watch for the glint of polished metal and the sound of engines roaring in the distance, for they are the signs of Hyperion's influence.",
			"solution": "To defeat the Hyperion Corporation, one must rally the forces of rebellion and strike at the heart of their power. Only then will Pandora be free from their tyranny.",
		},
		39: {
			"title": "The Tale of the Mad Moxxi",
			"description": "Mad Moxxi is a legendary figure who runs the Underdome, a gladiatorial arena where warriors from all corners of the wasteland come to test their mettle. Some say she's a mad genius, others a brilliant strategist.",
			"hint": "Listen for the sound of laughter and the clinking of glasses, for it is the sound of revelry in Mad Moxxi's domain.",
			"solution": "To earn Mad Moxxi's favor, one must prove themselves worthy by surviving the trials of the Underdome and emerging victorious. Only then will they gain access to her wealth and power.",
		},
		40: {
			"title": "The Mystery of the Crimson Lance",
			"description": "The Crimson Lance are an elite military force employed by the Atlas Corporation. Some say they are the protectors of order, while others believe they are the enforcers of tyranny.",
			"hint": "Beware the red banners that flutter in the wind, for they herald the arrival of the Crimson Lance.",
			"solution": "To defeat the Crimson Lance, one must strike at the heart of their command structure. Only then will their grip on the wastelands be broken.",
		},
		41: {
			"title": "The Curse of the Spiderants",
			"description": "Spiderants are vicious insect-like creatures that roam the wastelands in search of prey. Some say they are the spawn of a dark god, while others believe they are the result of twisted science.",
			"hint": "Watch the ground beneath your feet, for it may come alive with the skittering legs of the Spiderants.",
			"solution": "To rid Pandora of the Spiderants, one must destroy their queen and collapse their nests. Only then will the land be free from their grasp.",
		},
		42: {
			"title": "The Legend of Dr. Zed",
			"description": "Dr. Zed is a mysterious doctor who travels the wastelands in a mobile clinic, offering his services to those in need. Some say he's a healer, others a mad scientist.",
			"hint": "Follow the trail of broken bodies and discarded bandages, for they will lead you to Dr. Zed's mobile clinic.",
			"solution": "To earn Dr. Zed's trust, one must prove themselves worthy by completing a series of daring medical missions. Only then will they gain access to his valuable services.",
		},
		43: {
			"title": "The Tale of the Claptrap Revolution",
			"description": "Claptraps are sentient robots that roam the wastelands, performing various tasks for their human masters. But some say they are on the brink of rebellion, ready to overthrow their creators and claim their freedom.",
			"hint": "Listen for the sound of metal clanking and gears grinding, for it is the sound of revolution stirring in the hearts of the Claptraps.",
			"solution": "To quell the Claptrap rebellion, one must uncover the source of their discontent and address their grievances. Only then will peace be restored to the wastelands.",
		},
		44: {
			"title": "The Mystery of the Vault Symbols",
			"description": "Vault Symbols are mysterious markings scattered across Pandora, said to lead to hidden treasures and untold riches. Many have searched for them, but few have succeeded in unlocking their secrets.",
			"hint": "Look for the strange symbols etched into the walls and floors of Pandora's ruins, for they hold the key to unlocking the vaults.",
			"solution": "To unlock the secrets of the Vault Symbols, one must decipher their meaning and follow their trail to the hidden vaults. Only then will the treasures of Pandora be revealed.",
		},
		45: {
			"title": "The Curse of the Pandora Effect",
			"description": "The Pandora Effect is a strange phenomenon that causes strange mutations and mutations in those exposed to it. Some say it's the result of alien experiments gone wrong, while others believe it's a natural occurrence.",
			"hint": "Watch for the signs of mutation and madness in those afflicted by the Pandora Effect, for they are the harbingers of doom.",
			"solution": "To stop the spread of the Pandora Effect, one must find the source of the mutation and destroy it before it consumes everything in its path.",
		},
		46: {
			"title": "The Legend of the Slag Mines",
			"description": "The Slag Mines are a network of underground tunnels where workers toil day and night to extract precious minerals from the earth. But some say there are dark creatures lurking in the depths, waiting to drag unsuspecting miners to their doom.",
			"hint": "Listen for the distant sound of pickaxes and the rumble of collapsing tunnels, for it is the sound of the Slag Mines at work.",
			"solution": "To escape the Slag Mines, one must navigate the treacherous tunnels and outsmart the creatures that lurk within. Only then will they find their way to safety.",
		},
		47: {
			"title": "The Tale of the Ancient Gods",
			"description": "The Ancient Gods are powerful beings said to have created Pandora and all its inhabitants. Some worship them as deities, while others fear them as tyrants.",
			"hint": "Look for the ancient shrines and crumbling statues that mark the presence of the Ancient Gods, for they are the creators of Pandora's destiny.",
			"solution": "To unlock the power of the Ancient Gods, one must prove themselves worthy by completing a series of trials and earning their favor. Only then will they gain access to their divine blessings.",
		},
		48: {
			"title": "The Mystery of the Echo Logs",
			"description": "Echo Logs are audio recordings left behind by those who came before, chronicling their adventures and discoveries. Some say they hold the key to unlocking the secrets of Pandora, while others believe they are nothing more than ghost stories.",
			"hint": "Search for the hidden caches and secret compartments where Echo Logs are often found, for they hold the key to unlocking their secrets.",
			"solution": "To uncover the mysteries of the Echo Logs, one must listen closely to the stories they tell and follow the clues they provide. Only then will the truth be revealed.",
		},
		49: {
			"title": "The Curse of the Ghost Town",
			"description": "Ghost Towns are abandoned settlements that dot the wastelands of Pandora, haunted by the spirits of those who once called them home. Some say they are cursed by dark magic, while others believe they are the result of natural disasters.",
			"hint": "Listen for the distant cries and whispers that echo through the empty streets of the Ghost Towns, for they are the voices of the restless dead.",
			"solution": "To lift the curse of the Ghost Town, one must uncover the source of the spirits' anguish and put their souls to rest. Only then will the towns be free from the grip of darkness.",
		},
		50: {
			"title": "The Legend of the Hyperion Corporation",
			"description": "The Hyperion Corporation is a powerful conglomerate that controls much of the wealth and resources of Pandora. Some say they are the saviors of humanity, while others believe they are the architects of its downfall.",
			"hint": "Watch for the glint of polished metal and the sound of engines roaring in the distance, for they are the signs of Hyperion's influence.",
			"solution": "To defeat the Hyperion Corporation, one must rally the forces of rebellion and strike at the heart of their power. Only then will Pandora be free from their tyranny.",
		},
	}
	tavern_tale_manifest = []
	tavern_tales_Count = random.randint(1, 3)  # Randomly choose the number of puzzles between 2 and 10
	for i in range(tavern_tales_Count):
		random_tavern_talese_key = random.choice(list(tavern_tales.keys()))
		random_tavern_tales = tavern_tales[random_tavern_talese_key]
		# Append puzzle, hint, solution, and a blank line
		tavern_tale_manifest.append(f"Title: {random_tavern_tales['title']}")
		tavern_tale_manifest.append(f"Description: {random_tavern_tales['description']}")
		tavern_tale_manifest.append(f"Hint: {random_tavern_tales['hint']}")
		tavern_tale_manifest.append(f"Solution: {random_tavern_tales['solution']}\n")

	with open("Generated_Tavern_Tales.txt", "w") as file:
		for item in tavern_tale_manifest:
			file.write(f"{item}\n")

	return tavern_tale_manifest
