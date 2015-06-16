#Fizzbuzz.py (Lab 2) [Shane Roeseberg]

def main():
	while True:

		user = input("Enter a positive number (type 'stop' to stop): ")
		
		if user.upper() == "STOP":
			print("Stopped!")
			break

		user = int(user)

		start = 1
		end = user + 1

		if user < 0:
			print("Not a positive number!")

		number = 1
		while number <= user:
			if (number) % 5 == 0 and number % 3 == 0:
				print('{} FizzBuzz' .format(number))
			elif (number) % 3 == 0:
				print('{} Fizz' .format(number))
			elif (number) % 5 == 0:
				print('{} Buzz' .format(number))
			else:
				print(number)
				if number == user:
					break

			number += 1

if __name__ == '__main__':
	main()