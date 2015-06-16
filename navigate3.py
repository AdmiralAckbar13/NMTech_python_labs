#Navigate3.py (lab 6) [Shane Roeseberg]

import turtle
import time

start_time = time.clock()

print("== Navigate 3 ==")
print("\n")

def main():

	turtle_file = open("navigate3_data.py" , "r")
	array = turtle_file.read().split() #allows for simultaneous command execution
	turtle_file.close()
	make = turtle.Turtle()
	i = 0
	turtle_draw = [make]

	print("-----------------------------------")
	print("(navigate3_data.py file commands): ")
	print("-----------------------------------")

	for i in range(0, len(array), 2):
		direc = array[i]
		print(direc)
		numb = float(array[i + 1])
		print(numb)

		for x in turtle_draw:
			if direc == "forward":
				x.forward(numb)

			elif direc == "backward":
				x.backward(numb)

			elif direc == "left":
				x.left(numb)

			elif direc == "right":
				x.right(numb)

		if direc == "split":
			turtle_split(turtle_draw)

	print("\n")
	print("== Program Complete ==")
	print("\n")
	print("-----------------------------------")
	t = time.clock() - start_time
	print("Program runtime:", (round(t,2)), "seconds") #print amount of time program takes to run (in seconds)
	print("-----------------------------------")

def turtle_split(turtle_draw):
	for z in turtle_draw[:]:
		position = z.pos()
		bearing = z.heading()

		make = turtle.Turtle()
		make.speed(0)
		turtle_draw.append(make)

		make.penup()
		make.goto(position)
		make.pendown()
		make.right(360 - bearing + 40)

if __name__ == '__main__':
	main()