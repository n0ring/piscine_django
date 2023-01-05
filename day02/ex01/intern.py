
class Intern:
	class Coffe:
		def __str__(self) -> str:
			return 'This is the worst coffee you ever tasted.'

	def __init__(self, name='My name? I’m nobody, an intern, I have no name.') -> None:
		self.Name = name
	
	def __str__(self) -> str:
		return self.Name

	def work(self):
		raise Exception('I’m just an intern, I can’t do that...')

	def make_coffe(self):
		return self.Coffe()


def main():
	intern1 = Intern()
	intern_mark = Intern('Mark')

	print(intern1)
	print(intern_mark)
	print(intern_mark.make_coffe())
	try:
		intern1.work()
	except Exception as ex:
		print(ex)


if __name__ == '__main__':
	main()