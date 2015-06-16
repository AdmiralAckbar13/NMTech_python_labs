#Peasants b.).py (Lab 3) [Shane Roeseberg]
# b.) Recursive function implementing Russian peasant multiplication.  Call function expo()


def main(): #main input script

	while True:

		print("Type stop at any point to exit the program.")

		x = input("Please enter a number: ")
		y = input("Enter a number to multiply by the first number entered: ")

		if x.upper() == "STOP":
			print("Stopped!")
			break

		if y.upper() == "STOP": #'stop' command breaks program loop
			print("Stopped!")
			break

		x = int(x) #converting x (input) to integer
		y = int(y) #converting y (input) to integer

		print(expo(x,y)) #print function result

def expo(x,y):

	if y % 2 == 0: #if y (input) is even
		return (x ** 2) ** (y / 2)

	else: # if y (input) is odd
		return x * (x ** 2) ** (y - 1) / 2

if __name__ == '__main__':
	main()