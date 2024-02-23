import random

def generate_trauma():
	trauma_state = int(input("Is the trauma temperary(1) or permanent(2)? "))

	permanent_trauma = {
		1:"━━━Bad Reputation -  Word of how you fell in battle gets around. There’s a 25%% chance that any NPC you meet will have heard the embarrassing story of how you got beaten up, and will respect you less for it.━━━",
		2:"━━━How2English - You forget 10%% of your vocabulary. –1 on Talk Checks━━━",
		3:"━━━I Had a Bad Experience - You become terrified of the particular Enemy type who defeated you. In all future combats with this particular Enemy type, take -1 to all Accuracy Rolls.━━━",
		4:"━━━Trinket - Loss of sentimental item. Probably something important to the campaign.━━━",
		5:"━━━Least Favorite - The other players must determine your least favorite food/music/film/book/whatever. That is now your Vault Hunter’s FAVORITE thing in the world, and they will bring it up any time they can elegantly do so━━━",
		6:"━━━Scar Tissue - : Generates a horrific scar in the location where you took Damage. 25%% chance to be recognized when entering a town━━━",
		7:"━━━Touchy Feely - You have the insatiable urge to touch everything you see, including things you probably shouldn't. –1 on Interact Checks.━━━",
		8:"━━━Cool Eyepatch - Your character loses an eye and has to wear a badass eyepatch over the socket. You get a -2 to Search Checks, but a +3 to Interact Checks━━━",
		9:"━━━Love and Loss -  Your character is nursed back to health by an adorable, friendly animal of the BM’s choosing. The BM must then work the cute animal into the story, and then somehow tragically remove them within the next two sessions━━━",
		10:"━━━Synapse Oops - Brain farts are now a medical condition you have. –1 on Insight Checks━━━",
		11:"━━━Your Dad is Disapointed in you - Your dad hears about how you died. He is disappointed in you. Your mom is still proud of you, though.━━━",
		12:"━━━Willful Ignorance - Your Vault Hunter refuses to believe they fell in battle and assumes everyone is misremembering the event.━━━",
		13:"━━━Riverdance -  Metal clogs get stuck on your feet. –1 on Sneak Checks.━━━",
		14:"━━━Family Vengeance - Add “Jr.” to your character’s name. You are now your own child, avenging the death of your parent.━━━",
		15:"━━━Crybaby - Death hurts a lot, and your Vault Hunter cries when they think about it.━━━",
		16:"━━━No Ships Sherlock - Your trusty sleuthing cap got rakk poop on it. –1 on Search Checks.━━━",
		17:"━━━Fart Fartington - Your Vault Hunter’s name is now Fart Fartington. This can never be changed. If the Vault Hunters name is already Fart Fartington, “Fart Fartington” becomes their new nickname. Their name would now be Fart “Fart Fartington” Fartington━━━",
		18:"━━━18/20 - Your depth perception got pretty deep. –1 on Traverse Checks━━━",
		19:"━━━Unsteady Hands - Whenever you Swap guns, roll a d20. On a 1, the gun flies out of your hands and lands 2 Squares away.━━━",
		20:"━━━GodKiller - Your Vault Hunter blames the one TRULY responsible for their death: You. Your Vault Hunter now has a personal vendetta against you. The BM will insert you into the story somewhere and your Vault Hunter will do whatever is necessary to hunt you down and say some very harsh words.━━━",

	}
	temporary_trauma = {
		1:"━━━Bad Luck - The BREW-U malfunctions; roll on the Permanent table.━━━",
		2:"━━━Immersive - Must do a silly character voice. If you ever forget, take 1d6 Damage.━━━",
		3:"━━━Unloaded - : A random equipped gun doesn’t spawn with you. You will see it for sale at the next shop you find.━━━",
		4:"━━━Refractory -  Every time you roll a natural20 on an Attack Roll, fall asleep for the next turn━━━",
		5:"━━━No Boom - Current grenades is set to 0━━━",
		6:"━━━Stumbling - –1 on Talk and Traverse Checks for the day━━━",
		7:"━━━Pistol Perplexion - Your Vault Hunter is unable to tell the difference between guns and food.━━━",
		8:"━━━Health Draint - Health Drain: –5 max Health for the day━━━",
		9:"━━━Power Drain -  –20 max Shields for the day━━━",
		10:"━━━Punch Drunk - You must punch every non-combatant NPC you meet.━━━",
		11:"━━━Impatient - –1 on Search and Sneak Checks for the day━━━",
		12:"━━━Wellllll Hello There - : You must flirt with every NPC you meet. Including Bosses━━━",
		13:"━━━Catch-a-Phrase -  Your Vault Hunter is now desperate to popularize a stupid catch phrase they’ve just come up with.━━━",
		14:"━━━Four Hundred and Four - One of your non-current guns doesn’t respawn.━━━",
		15:"━━━Your hands Are Guns - Your currently equipped gun fuses into the bones of your hands. You no longer have fingers, or the ability to grab things.━━━",
		16:"━━━You Had Me At Roll For initiative - Your Vault Hunter is now unrequitedly in love with another player’s Vault Hunter. Before the end of the day, you must dramatically reveal your true feelings.━━━",
		17:"━━━Brain Freeze - –1 on Insight and Interact Checks for the day.━━━",
		18:"━━━The Best Policy - Your Vault Hunter is now incapable of lying for the rest of the day.━━━",
		19:"━━━Minor Issue - Your Vault Hunter is now four years old. All their stats are the same, but they look and speak like a four year old.━━━",
		20:"━━━You Are A Claptrap - A bolt of lightning strikes you and turns you into a Claptrap unit. All of your stats are reduced by 2 and you have to speak in an annoying voice until the end of the day.━━━",
	}

	if trauma_state == 1:
		trauma_value = random.randint(1,20)
		active_trauma = temporary_trauma[trauma_value]
		return active_trauma
	elif trauma_state >= 2:
		trauma_value = random.randint(1,20)
		active_trauma = permanent_trauma[trauma_value]
		return active_trauma
	