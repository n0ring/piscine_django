
def print_numbers():
	l: list = open('numbers.txt').read().strip().split(',')
	for el in l:
		print(el)


if __name__ == '__main__':
	print_numbers()