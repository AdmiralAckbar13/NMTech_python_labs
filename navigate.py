#Navigate.py (Lab 2) [Shane Roeseberg]

import turtle

def main():

	stored = []

	while True:
	    direction = input('Please enter a direction: ')
	    if direction == 'forward':
	        stored.append(turtle.forward(100))
	    elif direction == 'left':
	        degrees = input('How many degrees? ')
	        if int(degrees) < 0:
	            print('Invalid number, not moving.')
	        stored.append(turtle.left(int(degrees)))
	    elif direction == 'right':
	        degrees = input('How many degrees? ')
	        if int(degrees) < 0:
	            print('Invalid number, not moving.')
	        stored.append(turtle.right(int(degrees)))
	    elif direction == 'stop':

	        print("Stopped!")
	        break
	    else:
	        print('Invalid number, not moving.')
	         
if __name__ =='__main__':
	main()