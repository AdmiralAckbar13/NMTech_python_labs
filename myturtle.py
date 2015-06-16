#myturtle.py (lab 10) [Shane Roeseberg]

from turtle import Turtle

class better_turtle(Turtle):

	def __init__ (self):
		super().__init__()

	def forward(self, distance):
		if distance < 0:
			return
		super().forward(distance)

	def backward(self, distance):
		if distance < 0:
			return
		super().backward(distance)

	def left(self, distance):
		if distance < 0:
			return
		super().left(distance)
			

	def right(self, distance):
		if distance < 0:
			return
		super().right(distance)

	def regular_polygon(self, sides, length):

		angle = 360 / sides

		for variable in range(0, sides):
			self.forward(length)
			self.left(angle)