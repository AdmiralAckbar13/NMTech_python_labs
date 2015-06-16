#Polygons.py (Lab 2) [Shane Roeseberg]

import turtle

def main():

	sides = int(input("Enter number of sides: "))
	angle = 360 / sides

	for variable in range(0, sides):
		turtle.forward(100)
		turtle.left(angle)

	if variable == sides - 1:
		print("Complete!")

if __name__ == '__main__':
	main()