import sys

def error():
	print('Unknown state')
	exit(0)

def get_state_full(st: str):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	states_tuples = states.items()
	for el in states_tuples:
		if el[1] == st:
			return el[0]
	return None


def get_state_red(cap: str):
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	capitals = capital_cities.items()
	for el in capitals:
		if el[1] == cap:
			return el[0]
	return None


def main(cap: str):
	state_reduced: str
	state_full: str

	state_reduced = get_state_red(cap)
	if state_reduced == None:
		error()
	state_full = get_state_full(state_reduced)
	if state_full == None:
		error()
	print(state_full)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		exit(0)
	main(sys.argv[1].strip())