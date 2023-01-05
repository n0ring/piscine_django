import sys 
import re

def error(str='Unknown error'):
	print(str)
	exit(1)


def set_settings():
	lines: str = ''
	try:
		with open('settings.py') as file:
			lines = file.readlines()
	except:
		error("Problem with open file settings.py")
	for line in lines: 
		params = line.split('=')
		if len(params) != 2:
			error("File settings.py not valid")
		globals()[params[0].strip()] = params[1].strip()


def get_template(filename:str) -> str:
	content = ''
	try:
		with open(filename) as file:
			content = file.read()
	except:
		error(f'Problem with open file {filename}')
	return content


def is_template_name_valid(filename: str) -> bool:
	if (filename.endswith('.template') == False):
		return False


def replace_func(match_obj):
	var = match_obj.group(1)
	if var not in globals():
		error(f'Varible {var} not found')
	return globals().get(var)


def main():
	outputname = ''
	if len(sys.argv) != 2:
		error("wrong number of argu- ments")
	if is_template_name_valid(sys.argv[1]) == False:
		error("invalid filename")
	set_settings()
	template = get_template(sys.argv[1])
	result_page = re.sub(r"\{(.+)\}", replace_func, template)
	outputname = sys.argv[1].split('.')[0] + '.html'
	try: 
		with open(outputname, 'w') as outputfile:
			outputfile.write(result_page)
	except:
		error(f'Error with write to file {outputname}')


if __name__ == '__main__':
	main()