#Calculator.py (Lab 2) [Shane Roeseberg]

print("== Calculator ==")
print("\n")

import math

def main():

	while True:

		value = input("Enter a value to use (type 'stop' to stop): ")

		if value.upper() == "STOP":
			print("\n")
			print("== Program Exit ==")
			break

		operation = input("Which operation? sqrt (s), arcsin (a), arccos (c), arctan (t) (type 'stop' to stop): ")

		if value.upper() == "STOP":
			print("\n")
			print("== Program Exit ==")
			break

		value = float(value)

		if operation == "s":
		    if value < 0:
		        print("The input for a square root cannot be negative!")
		    else:
		        s = math.sqrt(value)
		        print('The square root of ' + str(value) + ' is ' + str(s))

		if operation == "a":
		    if value < -1 or value > 1:
		        print ("The input for arcsin must be between -1 and 1!")
		    else:
		        a = math.asin(value)
		        print('The arcsin of ' + str(value) + ' is ' + str(a))

		if operation == "c":
		    if value < -1 or value > 1:
		        print ("The input for arccos must be between -1 and 1!")
		    else:
		        c = math.acos(value)
		        print('The arccos of ' + str(value) + ' is ' + str(c))

		if operation == "t":
		    t = math.atan(value)
		    print('The arctan of ' + str(value) + ' is ' + str(t))

if __name__ == '__main__':
	main()