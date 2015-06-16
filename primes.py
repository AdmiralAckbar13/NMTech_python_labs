#Primes.py (Lab 2) [Shane Roeseberg]
#BROKEN (does not count the value 3 as prime)

import math

def main():
	while True:

		value = input("Enter a value (type 'stop' to stop): ")

		if value.upper() == "STOP":
			print("Stopped!")
			break

		value = int(value)	

		if value < 2:
			print("The value {} is not a prime value!" .format(value))

		else:
			for d in range (2, int(value / 2) + 1):
				if value % d == 0:
					print ("The value {} is not a prime value!" .format(value))
					break
				
if __name__ =='__main__':
	main()