class HotBeverage:
	def __init__(self, price=0.30, aname='hot beverage') -> None:
		self.price = price
		self.Aname = aname
	
	def description(self):
		return 'Just some hot water in a cup.'
	
	def __str__(self) -> str:
		return f'name : {self.Aname}\nprice : {self.price}\ndescription : {self.description()}'


class Coffee(HotBeverage):
	def __init__(self) -> None:
		super().__init__(0.40, 'coffe')

	def description(self):
		return 'A coffee, to stay awake.'


class Tea(HotBeverage):
	def __init__(self) -> None:
		super().__init__(aname='tea')


class Chocolate(HotBeverage):
	def __init__(self) -> None:
		super().__init__(0.50, 'chocolate')

	def description(self):
		return 'Chocolate, sweet chocolate...'


class Cappuccino(HotBeverage):
	def __init__(self) -> None:
		super().__init__(0.45, 'cappuccino')
	
	def description(self):
		return 'Un po’ di Italia nella sua tazza!'




def main():
	print(HotBeverage())
	print(Coffee())
	print(Tea())
	print(Chocolate())
	print(Cappuccino())

if __name__ == '__main__':
	main()