#Spiral.py (Lab 4) [Shane Roeseberg]

import turtle

print("== Spiral ==")

def main():

	distance = 11
	angle = 10

	for i in range(250):
	    turtle.forward(distance)
	    turtle.left(angle)
	    distance = distance + .20

	if i == 249:
		print("== Program Completed ==")

if __name__ == '__main__':
	main()