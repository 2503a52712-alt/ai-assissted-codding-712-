"""Task 4: Inventory Class using TDD."""


# Tests are written first to describe the required behavior.
def test_inventory():
	inv = Inventory()

	inv.add_item("Pen", 10)
	assert inv.get_stock("Pen") == 10

	inv.remove_item("Pen", 5)
	assert inv.get_stock("Pen") == 5

	inv.add_item("Book", 3)
	assert inv.get_stock("Book") == 3

	inv.add_item("Pen", 2)
	inv.add_item("Pen", 3)
	assert inv.get_stock("Pen") == 10  # Adding an existing item increases stock.

	assert inv.get_stock("Pencil") == 0  # Missing items have no stock.

	inv.remove_item("Book", 10)
	assert inv.get_stock("Book") == 0  # Stock cannot become negative.


class Inventory:
	def __init__(self):
		# Store each item name and its quantity in a dictionary.
		self.items = {}

	def add_item(self, name, quantity):
		"""Add quantity to an item, creating it if needed."""
		if name in self.items:
			self.items[name] += quantity
		else:
			self.items[name] = quantity

	def remove_item(self, name, quantity):
		"""Remove quantity without allowing stock to become negative."""
		if name in self.items:
			self.items[name] -= quantity
			if self.items[name] < 0:
				self.items[name] = 0

	def get_stock(self, name):
		"""Return the current quantity, or zero for an unknown item."""
		return self.items.get(name, 0)


test_inventory()
print("All Task 4 tests passed!")
