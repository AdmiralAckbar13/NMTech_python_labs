#Shapes.py (Lab 1) [Shane Roeseberg]

import math

def main():
	while True:

		radius = input("Please input the radius of the circle (type 'stop' to stop): ") #Get input from user.
		
		if radius.upper() == "STOP":
			print ("Stopped!")
			break

		#Use math.pi for pi

		radius = float(radius)

		#Calculate and display the circumference and area of the circle.

		circumference = 2 * math.pi * radius #Circumference formula.

		print("The circumference of the circle is: " + '{0:.4g}' .format(circumference))

		area = math.pi * radius ** 2 #Area forumula.

		print("The area of the circle is: " + '{0:.4g}' .format(area)) 

		width = input('Please input the width of the box: ')
		height = input('Please input the height of the box: ')
		length = input('Please input the length of the box: ')

		width = float(width)
		height = float(height)
		length = float(length)

		#Calculate and display the surface area and volume of the box.

		surfacearea = 2 * length * width + 2 * length * height + 2 * width * height #Surface area forumala.

		print("The surface area of the box is: " + str(surfacearea))

		volume = length * width * height #Volume formula.

		print("The volume of the box is: " + str(volume))

if __name__ == '__main__':
	main()