#Star (Lab 2) [Shane Roeseberg]

import turtle

def main():

	counter = 0

	turtle.right(36)

	while counter < 6:
		turtle.right(144)
		turtle.forward(100)
		
		counter = counter + 1

		if counter > 5:
			print("Complete!")

if __name__ == '__main__':
	main()