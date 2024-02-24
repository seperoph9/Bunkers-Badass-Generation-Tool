import random

#
# Generate Gun
#
def generate_gun(checkrarity):
	gentype = int(checkrarity)

	gun_types = {
		1: "Pistol",
		2: "Submachine Gun",
		3: "Shotgun",
		4: "Combat Rifle",
		5: "Sniper Rifle",
		6: "Rocket Launcher"
	}

	guilds_pistol = {
		1: "Skuldugger's",
		2: "Feriore's",
		3: "Dahlia's",
		4: "Blackpowder's",
		5: "Alas's",
		6: "Malefactor's",
		7: "Stoker's",
		8: "Hyperius's"
	}

	guilds_submachine_gun = {
		1: "Malefactor's",
		2: "Skuldugger's",
		3: "Hyperius's",
		4: "Feriore's",
		5: "Torgue's",
		6: "Dahlia's",
		7: "Skuldugger's",
		8: "Feriore's"
	}

	guilds_shotgun = {
		1: "Hyperius's",
		2: "Blackpowder's",
		3: "Skuldugger's",
		4: "Feriore's",
		5: "Torgue's",
		6: "Stoker's",
		7: "Alas's",
		8: "Malefactor's"
	}

	guilds_combat_rifle = {
		1: "Feriore's",
		2: "Dahlia's",
		3: "Torgue's",
		4: "Stoker's",
		5: "Hyperius's",
		6: "Alas's",
		7: "Dahlia's",
		8: "Alas's"
	}

	guilds_sniper_rifle = {
		1: "Skuldugger's",
		2: "Alas's",
		3: "Blackpowder's",
		4: "Malefactor's",
		5: "Dahlia's",
		6: "Hyperius's",
		7: "Stoker's",
		8: "Torgue's"
	}

	guilds_rocket_launcher = {
		1: "Stoker's",
		2: "Torgue's",
		3: "Malefactor's",
		4: "Malefactor's",
		5: "Stoker's",
		6: "Torgue's",
		7: "Malefactor's",
		8: "Hyperius's"
	}

	guilds = {
		1: "Skuldugger's",
		2: "Feriore's",
		3: "Dahlia's",
		4: "Blackpowder's",
		5: "Alas's",
		6: "Malefactor's",
		7: "Stonker's",
		8: "Hyperius's"
	}

	rarity_table = {
		1: {
			1: "Common",
			2: "Common (Element Roll)",
			3: "Common (Element Roll)",
			4: "Uncommon",
			5: "Uncommon (Element Roll)",
			6: "Rare"
		},
		2: {
			1: "Common",
			2: "Common (Element Roll)",
			3: "Uncommon",
			4: "Uncommon (Element Roll)",
			5: "Rare (Element Roll)",
			6: "Epic"
		},
		3: {
			1: "Uncommon (Element Roll)",
			2: "Rare",
			3: "Rare (Element Roll)",
			4: "Epic",
			5: "Epic (Element Roll)",
			6: "Legendary (Element Roll)"
		},
		4: {
			1: "Rare (Element Roll)",
			2: "Rare (Element Roll)",
			3: "Epic (Element Roll)",
			4: "Epic (Element Roll)",
			5: "Legendary (Element Roll)",
			6: "Legendary (Element Roll)"
		}
	}

	element_table = {
		"Common": {
			1: "",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:"",14:"",15:"",16:"",17:"",18:"",19:"",20:"",21:"",22:"",23:"",24:"",25:"",26:"",27:"",28:"",29:"",30:"",31:"",32:"",33:"",34:"",35:"",36:"",37:"",38:"",39:"",40:"",41:"",42:"",43:"",44:"",45:"",46:"",47:"",48:"",49:"",50:"",51:"",52:"",53:"",54:"",55:"",56:"",57:"",58:"",59:"",60:"",61:"",62:"",63:"",64:"",65:"",66:"",67:"",68:"",69:"",70:"",71:"",72:"",73:"",74:"",75:"",76:"",77:"",78:"",79:"",80:"",81:"",82:"",83:"",84:"",85:"",
			86: "Radiation",87:"Radiation",88:"Radiation",89:"Radiation",90:"Radiation",
			91: "Corrosive",92:"Corrosive",
			93: "Shock",94:"Shock",
			95: "Explosive",96:"Explosive",
			97: "Incendiary",98:"Incendiary",
			99: "Cryo",100:"Cryo"
		},
		"Uncommon": {
			1: "",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:"",14:"",15:"",16:"",17:"",18:"",19:"",20:"",21:"",22:"",23:"",24:"",25:"",26:"",27:"",28:"",29:"",30:"",31:"",32:"",33:"",34:"",35:"",36:"",37:"",38:"",39:"",40:"",41:"",42:"",43:"",44:"",45:"",46:"",47:"",48:"",49:"",50:"",51:"",52:"",53:"",54:"",55:"",
			56: "Radiation",57:"Radiation",58:"Radiation",59:"Radiation",60:"Radiation",
			61: "Corrosive",62:"Corrosive",63:"Corrosive",64:"Corrosive",65:"Corrosive",
			66: "Shock",67:"Shock",68:"Shock",69:"Shock",70:"Shock",
			71: "Explosive",72:"Explosive",73:"Explosive",74:"Explosive",75:"Explosive",
			76: "Incendiary",77:"Incendiary",78:"Incendiary",79:"Incendiary",80:"Incendiary",
			81: "Cryo",82:"Cryo",83:"Cryo",84:"Cryo",85:"Cryo",
			86: "Radiation(+1d6)",87:"Radiation(+1d6)",88:"Radiation(+1d6)",89:"Radiation(+1d6)",90:"Radiation(+1d6)",
			91: "Corrosive(+1d6)",92:"Corrosive(+1d6)",
			93: "Shock(+1d6)",94:"Shock(+1d6)",
			95: "Explosive(+1d6)",96:"Explosive(+1d6)",
			97: "Incendiary(+1d6)",98:"Incendiary(+1d6)",
			99: "Cryo(+1d6)",100:"Cryo(+1d6)"
		},
		"Rare": {
			1: "",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:"",14:"",15:"",16:"",17:"",18:"",19:"",20:"",21:"",22:"",23:"",24:"",25:"",
			26: "Radiation",27:"Radiation",28:"Radiation",29:"Radiation",30:"Radiation",
			31: "Corrosive",32:"Corrosive",33:"Corrosive",34:"Corrosive",35:"Corrosive",
			36: "Shock",37:"Shock",38:"Shock",39:"Shock",40:"Shock",
			41: "Explosive",42:"Explosive",43:"Explosive",44:"Explosive",45:"Explosive",
			46: "Incendiary",47:"Incendiary",48:"Incendiary",49:"Incendiary",50:"Incendiary",
			51: "Cryo",52:"Cryo",53:"Cryo",54:"Cryo",55:"Cryo",
			56: "Radiation(+1d6)",57:"Radiation(+1d6)",58:"Radiation(+1d6)",59:"Radiation(+1d6)",60:"Radiation(+1d6)",61:"Corrosive(+1d6)",62:"Corrosive(+1d6)",63:"Corrosive(+1d6)",64:"Corrosive(+1d6)",65:"Corrosive(+1d6)",
			66: "Shock(+1d6)",67:"Shock(+1d6)",68:"Shock(+1d6)",69:"Shock(+1d6)",70:"Shock(+1d6)",
			71: "Explosive(+1d6)",72:"Explosive(+1d6)",73:"Explosive(+1d6)",74:"Explosive(+1d6)",75:"Explosive(+1d6)",
			76: "Incendiary(+1d6)",77:"Incendiary(+1d6)",78:"Incendiary(+1d6)",79:"Incendiary(+1d6)",80:"Incendiary(+1d6)",
			81: "Cryo(+1d6)",82:"Cryo(+1d6)",83:"Cryo(+1d6)",84:"Cryo(+1d6)",85:"Cryo(+1d6)",
			86: "Radiation(+2d6)",87:"Radiation(+2d6)",88:"Radiation(+2d6)",89:"Radiation(+2d6)",90:"Radiation(+2d6)",
			91: "Corrosive(+2d6)",92:"Corrosive(+2d6)",
			93: "Shock(+2d6)",94:"Shock(+2d6)",
			95: "Explosive(+2d6)",96:"Explosive(+2d6)",
			97: "Incendiary(+2d6)",98:"Incendiary(+2d6)",
			99: "Cryo(+2d6)",100:"Cryo(+2d6)"
		},
		"Epic": {
			1: "",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",
			11: "Radiation",12:"Radiation",13:"Radiation",14:"Radiation",15:"Radiation",
			16: "Corrosive",17:"Corrosive",18:"Corrosive",19:"Corrosive",20:"Corrosive",
			21: "Shock",22:"Shock",23:"Shock",24:"Shock",25:"Shock",
			26: "Explosive",27:"Explosive",28:"Explosive",29:"Explosive",30:"Explosive",
			31: "Incendiary",32:"Incendiary",33:"Incendiary",34:"Incendiary",35:"Incendiary",
			36: "Cryo",37:"Cryo",38:"Cryo",39:"Cryo",40:"Cryo",
			41: "Radiation(+1d6)",42:"Radiation(+1d6)",43:"Radiation(+1d6)",44:"Radiation(+1d6)",45:"Radiation(+1d6)",
			46: "Corrosive(+1d6)",47:"Corrosive(+1d6)",48:"Corrosive(+1d6)",49:"Corrosive(+1d6)",50:"Corrosive(+1d6)",
			51: "Shock(+1d6)",52:"Shock(+1d6)",53:"Shock(+1d6)",54:"Shock(+1d6)",55:"Shock(+1d6)",
			56: "Explosive(+1d6)",57:"Explosive(+1d6)",58:"Explosive(+1d6)",59:"Explosive(+1d6)",60:"Explosive(+1d6)",
			61: "Incendiary(+1d6)",62:"Incendiary(+1d6)",63:"Incendiary(+1d6)",64:"Incendiary(+1d6)",65:"Incendiary(+1d6)",
			66: "Cryo(+1d6)",67:"Cryo(+1d6)",68:"Cryo(+1d6)",69:"Cryo(+1d6)",70:"Cryo(+1d6)",
			71: "Radiation(+2d6)",72:"Radiation(+2d6)",73:"Radiation(+2d6)",74:"Radiation(+2d6)",75:"Radiation(+2d6)",
			76: "Corrosive(+2d6)",77:"Corrosive(+2d6)",78:"Corrosive(+2d6)",79:"Corrosive(+2d6)",80:"Corrosive(+2d6)",
			81: "Shock(+2d6)",82:"Shock(+2d6)",83:"Shock(+2d6)",84:"Shock(+2d6)",85:"Shock(+2d6)",
			86: "Explosive(+2d6)",87:"Explosive(+2d6)",88:"Explosive(+2d6)",89:"Explosive(+2d6)",90:"Explosive(+2d6)",
			91: "Incendiary(+2d6)",92:"Incendiary(+2d6)",
			93: "Cryo(+2d6)",94:"Cryo(+2d6)",
			95: "Radiation+Incendiary",96:"Radiation+Incendiary",
			97: "Shock+Corrosive",98:"Shock+Corrosive",
			99: "Explosive+Cryo",100:"Explosive+Cryo"
		},
		"Legendary": {
			1: "",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",
			11: "Radiation",12:"Radiation",13:"Radiation",14:"Radiation",15:"Radiation",
			16: "Corrosive",17:"Corrosive",18:"Corrosive",19:"Corrosive",20:"Corrosive",
			21: "Shock",22:"Shock",23:"Shock",24:"Shock",25:"Shock",
			26: "Explosive",27:"Explosive",28:"Explosive",29:"Explosive",30:"Explosive",
			31: "Incendiary",32:"Incendiary",33:"Incendiary",34:"Incendiary",35:"Incendiary",
			36: "Cryo",37:"Cryo",38:"Cryo",39:"Cryo",40:"Cryo",
			41: "Radiation(+1d6)",42:"Radiation(+1d6)",43:"Radiation(+1d6)",44:"Radiation(+1d6)",45:"Radiation(+1d6)",
			46: "Corrosive(+1d6)",47:"Corrosive(+1d6)",48:"Corrosive(+1d6)",49:"Corrosive(+1d6)",50:"Corrosive(+1d6)",
			51: "Shock(+1d6)",52:"Shock(+1d6)",53:"Shock(+1d6)",54:"Shock(+1d6)",55:"Shock(+1d6)",
			56: "Explosive(+1d6)",57:"Explosive(+1d6)",58:"Explosive(+1d6)",59:"Explosive(+1d6)",60:"Explosive(+1d6)",
			61: "Incendiary(+1d6)",62:"Incendiary(+1d6)",63:"Incendiary(+1d6)",64:"Incendiary(+1d6)",65:"Incendiary(+1d6)",
			66: "Cryo(+1d6)",67:"Cryo(+1d6)",68:"Cryo(+1d6)",69:"Cryo(+1d6)",70:"Cryo(+1d6)",
			71: "Radiation(+2d6)",72:"Radiation(+2d6)",73:"Radiation(+2d6)",74:"Radiation(+2d6)",75:"Radiation(+2d6)",
			76: "Corrosive(+2d6)",77:"Corrosive(+2d6)",78:"Corrosive(+2d6)",79:"Corrosive(+2d6)",80:"Corrosive(+2d6)",
			81: "Shock(+2d6)",82:"Shock(+2d6)",83:"Shock(+2d6)",84:"Shock(+2d6)",85:"Shock(+2d6)",
			86: "Explosive(+2d6)",87:"Explosive(+2d6)",88:"Explosive(+2d6)",89:"Explosive(+2d6)",90:"Explosive(+2d6)",
			91: "Incendiary(+2d6)",92:"Incendiary(+2d6)",
			93: "Cryo(+2d6)",94:"Cryo(+2d6)",
			95: "Radiation+Incendiary",96:"Radiation+Incendiary",
			97: "Shock+Corrosive",98:"Shock+Corrosive",
			99: "Explosive+Cryo",100:"Explosive+Cryo"
		}
	}

	gun_type_roll = random.randint(1, 8)
	if gun_type_roll == 7:
		gun_type = "Player Favored Weapon"# Assuming this is the case for special roll
		guild = "BM's Guild Choice"
	elif gun_type_roll == 8:
		gun_type = "Player Favored Weapon"# Assuming this is the case for special roll
		guild = "BM's Guild Choice"
	else:
		gun_type = gun_types[gun_type_roll] 

	if gun_type == "Pistol":
		guild_roll = random.randint(1, 8)
		guild = guilds_pistol[guild_roll]
	elif gun_type == "Submachine Gun":
		guild_roll = random.randint(1, 8)
		guild = guilds_submachine_gun[guild_roll]
	elif gun_type == "Shotgun":
		guild_roll = random.randint(1, 8)
		guild = guilds_shotgun[guild_roll]
	elif gun_type == "Combat Rifle":
		guild_roll = random.randint(1, 8)
		guild = guilds_combat_rifle[guild_roll]
	elif gun_type == "Sniper Rifle":
		guild_roll = random.randint(1, 8)
		guild = guilds_sniper_rifle[guild_roll]
	elif gun_type == "Rocket Launcher":
		guild_roll = random.randint(1, 8)
		guild = guilds_rocket_launcher[guild_roll]
	else:
		pass
	rarity_roll = random.randint(1, 4)
	rarity_result = rarity_table[rarity_roll]
	rarity = random.choice(list(rarity_result.values()))
	if gentype == 0:
		pass
	if gentype > 0:
		elementrollcheck = random.randint(1,2)
		if elementrollcheck == 1:
			if gentype == 1:
				rarity = 'Common'
			if gentype == 2:
				rarity = 'Uncommon'
			if gentype == 3:
				rarity = 'Rare'
			if gentype == 4:
				rarity = 'Epic'
			if gentype == 5:
				rarity = 'Legendary'
		if elementrollcheck == 2:
			if gentype == 1:
				rarity = 'Common (Element Roll)'
			if gentype == 2:
				rarity = 'Uncommon (Element Roll)'
			if gentype == 3:
				rarity = 'Rare (Element Roll)'
			if gentype == 4:
				rarity = 'Epic (Element Roll)'
			if gentype == 5:
				rarity = 'Legendary (Element Roll)'
	
	if rarity.find('Element Roll'):
		element_roll = random.randint(1, 100)
		element_rarity = rarity.split()[0]
		element_result = element_table[element_rarity]
		element = element_result[element_roll]
		rarity = rarity.split()[0]
	if guild.find('Malefactor'):
		element_roll = random.randint(1, 100)
		element_rarity = rarity.split()[0]
		element_result = element_table[element_rarity]
		element = element_result[element_roll]
		if element == "":
			while element == "":
				element_roll = random.randint(1, 100)
				element_rarity = rarity.split()[0]
				element_result = element_table[element_rarity]
				element = element_result[element_roll]
	if guild.find('Alas'):
		pass
	if guild.find('Blackpowder'):
		pass
			
		#rarity = rarity.replace('(Element Roll)',"")
	else:
		element = ""

	guild_alas = {
		'Common':"+1 DMG Mod",
		'Uncommon':"+2 DMG Mod",
		'Rare':"+3 DMG Mod",
		'Epic':"+3 DMG Mod",
		'Legendary':"+4 DMG Mod",
	}
	guild_skulldugger = {
		'Common':"+2 DMG Mod, Overheat 1d4",
		'Uncommon':"+3 DMG Mod, Overheat 1d6",
		'Rare':"+4 DMG Mod, Overheat 1d8",
		'Epic':"+5 DMG Mod, Overheat 1d10",
		'Legendary':"+6 DMG Mod, Overheat 1d12",
	}
	guild_dahlia = {
		'Common':"Burst +1 Hit",
		'Uncommon':"Burst +1 Hit, +1 ACC Mod",
		'Rare':"Burst +1 Hit, +2 ACC Mod",
		'Epic':"Burst +1 Hit, +3 ACC Mod",
		'Legendary':"Burst +1 Hit, +4 ACC mod",
	}
	guild_blackpowder = {
		'Common':"+2 ACC mod, +2 Crit Damage",
		'Uncommon':"+2 ACC mod, +3 Crit Damage",
		'Rare':"+2 ACC mod, +4 Crit Damage",
		'Epic':"+2 ACC mod, +5 Crit Damage",
		'Legendary':"+2 ACC mod, +6 Crit Damage",
	}
	guild_malefactor = {
		'Common':"Element Roll, -2 DMG Mod",
		'Uncommon':"Element Roll,  -1 DMG Mod",
		'Rare':"10%% Element Roll ",
		'Epic':"15%% Element Roll ",
		'Legendary':"20%% Element Roll",
	}
	guild_hyperius = {
		'Common':"+1 ACC Mod, -2 DMG Mod",
		'Uncommon':"+2 ACC Mod, -2 DMG Mod",
		'Rare':"+3 ACC Mod, -2 DMG Mod",
		'Epic':"+4 ACC Mod, -2 DMG Mod",
		'Legendary':"+5 ACC Mod, -2 DMG Mod",
	}
	guild_feriore = {
		'Common':"Swap/Reload 1d4 Grenade Damage, -3 ACC Mod",
		'Uncommon':"Swap/Reload 1d6 Grenade Damage, -3 ACC Mod",
		'Rare':"Swap/Reload 1d8 Grenade Damage, -2 ACC Mod",
		'Epic':"Swap/Reload 1d10 Grenade Damage, -2 ACC Mod",
		'Legendary':"Swap/Reload 1d12 Grenade Damage, -1 ACC Mod",
	}
	guild_torgue = {
		'Common':"Splash, -4 ACC Mod",
		'Uncommon':"Splash, -3 ACC Mod",
		'Rare':"Splash, -2 ACC Mod",
		'Epic':"Splash, -1 ACC Mod",
		'Legendary':"Splash",
	}
	guild_stoker = {
		'Common':"Extra Attack, -3 ACC Mod",
		'Uncommon':"Extra Attack, -2 ACC Mod",
		'Rare':"Extra Attack, -1 ACC Mod",
		'Epic':"Extra Attack",
		'Legendary':"Extra Attack, Extra movement",
	}
	guild_BM_Choice_Guild = {
		'Common':"(Effect Guild Dependant)",
		'Uncommon':"(Effect Guild Dependant)",
		'Rare':"(Effect Guild Dependant)",
		'Epic':"(Effect Guild Dependant)",
		'Legendary':"(Effect Guild Dependant)",
	}
	guilds_dict = {
		"Alas's": guild_alas,
		"Skuldugger's": guild_skulldugger,
		"Dahlia's": guild_dahlia,
		"Blackpowder's": guild_blackpowder,
		"Malefactor's": guild_malefactor,
		"Hyperius's": guild_hyperius,
		"Feriore's": guild_feriore,
		"Torgue's": guild_torgue,
		"Stoker's": guild_stoker,
		"BM's Guild Choice" : guild_BM_Choice_Guild
	}


	# Check if the guild is present in the guilds dictionary
	guild_effect = ""
	selected_guild = None

	# Get Guild Type
	if guilds_dict.get(guild):
		selected_guild = guilds_dict[guild]
	else:
		print("Guild not found:", guild)

	# Get Rarity Stats
	if selected_guild and selected_guild.get(rarity):
		guild_effect = selected_guild[rarity]
	else:
		print("Rarity not found for the guild:", guild)

	return f"{guild} {rarity} {element} {gun_type} - Effect: {guild_effect}"