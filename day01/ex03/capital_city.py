import sys	

def main(state: str):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if state not in states or states[state] not in capital_cities:
		print('Unknown state')
		exit(0)
	print(capital_cities[states[state]])


if __name__ == '__main__':
	if len(sys.argv) != 2:
		exit(0)
	main(sys.argv[1].strip())