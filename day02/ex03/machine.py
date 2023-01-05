import beverage
import random

class CoffeeMachine:
	class EmptyCup(beverage.HotBeverage):
		def __init__(self) -> None:
			super().__init__(0.90, 'empty cup')
		
		def description(self):
			return 'An empty cup?! Gimme my money back!'
	
	class BrokenMachineException(Exception):
		def __init__(self) -> None:
			super().__init__('This coffee machine has to be repaired.')

	def __init__(self) -> None:
		self.count = 0

	def repair(self):
		self.count = 0

	def serve(self, drink: beverage.HotBeverage):
		if self.count == 10:
			raise self.BrokenMachineException()
		drink_class = drink.__class__
		self.count += 1
		if random.randint(0, 4) == 0:
			return self.EmptyCup()
		return drink_class()


if __name__ == '__main__':
	cm = CoffeeMachine()
	list_of_drinks = [beverage.Cappuccino(), beverage.Chocolate(), beverage.Coffee(), beverage.Tea()]

	for _ in range(12):
		try:
			print(cm.serve(random.choice(list_of_drinks)))
		except Exception as exp:
			print("----")
			print(exp)
			print("----")
			cm.repair()
	

