import sys	

def main(arg_list: list[str]):
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
	new_states: dict = {}
	new_capitals: dict = {}
	for state_name in states:
		capital_name = capital_cities[states[state_name]]
		new_states[state_name.lower()] = capital_name
		new_capitals[capital_name.lower()] = state_name
	for el in arg_list:
		current = el.strip().lower()
		if len(current) == 0:
			continue
		if current not in new_states and current not in new_capitals:
			print(f'{el.strip()} is neither a capital city nor a state')
			continue
		if current in new_states:
			print(f'{new_states[current]} is the capital of {new_capitals[new_states[current].lower()]}')
		elif current in new_capitals:
			print(f'{new_states[new_capitals[current].lower()]} is the capital of {new_capitals[current]}')


if __name__ == '__main__':
	if len(sys.argv) != 2:
		exit(0)
	if ',,' in sys.argv[1]:
		exit(0)
	arg_list: list = sys.argv[1].split(',')
	main(arg_list)
