
def get_td(obj: dict[str, str]):
	return f'''
	<td class="filled"> 
		<ul>
			<li class="small">  <strong>{obj['small']} </strong> </li>
			<li class="small"> No. {obj['number']} </li>
			<li class="small"> {obj['molar'][0:5]} </li>
		</ul>
		<h4 class="el_name"> {obj['name']} </h4>
	</td>'''

def get_empty_td(count, ch=''):
	return f'''{f'<td class="empty" colspan="{count}">{ch}</td>'}
	'''

def get_data(line: str):
	return line.split(':')[1].strip()

def parse_line(line:str) -> dict:
	obj = {}
	l = line.split(',')
	obj['name'] = l[0].split('=')[0].strip()
	obj['number'] = get_data(l[1])
	obj['small'] = get_data(l[2])
	obj['molar'] = get_data(l[3])
	obj['electron'] = get_data(l[4])
	return obj


def get_tds():
	line_count = 18
	file = open('periodic_table.txt')
	count = 0
	result = '<tr>'
	lines = file.readlines()
	for line in lines:
		if count >= line_count and count % line_count == 0:
			result += '<tr>'
		if count == 1:
			result += get_empty_td(16)
			count += 16
		if count == 20 or count == 38:
			result += get_empty_td(10)
			count += 10
		if count == 92:
			result += get_empty_td(1, '*')
			count += 1
		if count == 110:
			result += get_empty_td(1, '**')
			count += 1
		result += get_td(parse_line(line.strip()))
		line = file.readline()
		count += 1
		if count >= line_count and count % line_count == 0:
			result += '</tr>'
	file.close()
	return result


def get_html_page():
	return f'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Periodic table of the elements</title>
	<style>
		{'li { font-size: 8px; margin: 0px; padding: 0px;}'}
		{'.filled { border: 1px solid black;}'}
		{'ul {list-style-type: none;  padding: 0; margin: 0;}'}
		{'.empty {text-align: center;vertical-align: middle;}'}
		{'.small {font-size: 16px;}'}
		{'.el_name  {font-size: 0.9em; color: #424242;}'}
	</style>
</head>
<body>
	<table>
		{get_tds()}
	</table>
</body>
</html>'''


def main():
	s = get_html_page()
	file = open("periodic_table.html", 'w')
	file.write(s)
	file.close()


if __name__ == '__main__':
	main()