
def my_var():
	num: int = 42;
	s: str = '42'
	s2: str = 'quarante-deux'
	f: float = 42.0
	b: bool = True
	l: list = [42]
	d: dict = {42: 42}
	t: tuple = (42, )
	st: set = {'set()'}
	print(num, 'has a type', type(num))
	print(s, 'has a type', type(s))
	print(s2, 'has a type', type(s2))
	print(f, 'has a type', type(f))
	print(b, 'has a type', type(b))
	print(l, 'has a type', type(l))
	print(d, 'has a type', type(d))
	print(t, 'has a type', type(t))
	for el in st: 
		print(el, 'has a type', type(st))



if __name__ == '__main__':
	my_var()