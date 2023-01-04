
def get_new_dict(d: dict[str, str]):
	new_dict: dict[int, list[str]] = {}
	for key in d:
		year = int(d[key])
		if year not in new_dict:
			new_dict[year] = []
		new_dict[year].append(key)
	
	for key in new_dict:
		new_dict[key].sort()
	
	return new_dict


def main():
	d: dict[str, str] = {
		'Hendrix' : '1942', 'Allman' : '1946',
		'King' : '1925', 'Clapton' : '1945',
		'Johnson' : '1911', 'Berry' : '1926',
		'Vaughan' : '1954', 'Cooder' : '1947',
		'Page' : '1944', 'Richards' : '1943',
		'Hammett' : '1962', 'Cobain' : '1967',
		'Garcia' : '1942', 'Beck' : '1944',
		'Santana' : '1947', 'Ramone' : '1948',
		'White' : '1975', 'Frusciante': '1970',
		'Thompson' : '1949', 'Burton' : '1939',
	}
	new_dict: dict[int, list[str]] = get_new_dict(d)
	sorted_list = list(new_dict.keys())
	sorted_list.sort()
	for key in sorted_list:
		for el in new_dict[key]:
			print(el)


if __name__ == '__main__':
	main() 