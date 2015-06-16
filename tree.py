#tree.py (lab 10) [Shane Roeseberg]

class Tree():
	point = None
	def __init__ (self, datum, left = None, right = None):
		self.datum = datum
		self.left = left
		self.right = right

	def height(self):
		if self.left == None:

			len_left = 0
		else:
			len_left = self.left.height()
		if self.right == None:
			len_right = 0
		else:
			len_right = self.right.height()
		return 1 + len_right + len_left

	def add_item(self, item):
		if self.left == None:
			len_left = 0
		else:
			len_left = self.left.height()
		if self.right == None:
			len_right = 0
		else:
			len_right = self.right.height()

		if len_left >= len_right:
			if len_left == 0:
				self.left = Tree(item)
			else:
				self.left.add_item(item)
		else:
			if len_right == 0:
				self.right = Tree(item)
			else:
				self.right.add_item(item)
	def __iter__(self):
		self.point = None
		return self

	def __next__(self):
		if self.point == None:
			self.point = 1
			return self
		elif self.point == 1:
			if self.left == None and self.right == None:
				raise StopIteration
			try:
				return self.left.__next__()
			except (StopIteration):
				self.point = 2
		if self.point == 2:
			if self.right == None:
				raise StopIteration
			try:
				return self.right.__next__()
			except (StopIteration):
				raise StopIteration
