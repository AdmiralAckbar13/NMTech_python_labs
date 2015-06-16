#Sums.py (Lab 2) [Shane Roeseberg]

def main():

	total = 0

	while True:

		value = input("Enter a number (type 'exit' to print sum): ")

		if value.upper() == "EXIT":
			print("Sum of numbers: " + str(total))
			break

		total = total + float(value)

if __name__ == '__main__':
	main()