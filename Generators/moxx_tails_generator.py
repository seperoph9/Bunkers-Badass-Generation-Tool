import random
def generate_moxx_tails():

	moxx_tails_drinks = {
		1:"Hey Sugar",
		2:"Vamp Vermouth",
		3:"Quadruple Sec",
		4:"Kill-You-A",
		5:"Sonic Water",
		6:"Drub Soda",
		7:"Gamaretto",
		8:"Cream of Kapow",
		9:"Dragnac",
		10:"Big Bad Biters",
	}
	moxx_tails_drink_selection = random.randint(1,len(moxx_tails_drinks))
	moxx_tails_selected_drink = moxx_tails_drinks[moxx_tails_drink_selection]
	return moxx_tails_selected_drink