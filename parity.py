#Parity.py (Lab 4) [Shane Roeseberg]

def main():
	
	print("== Parity ==")
	print("Type 'stop' at any point to produce output and exit the program.")
	print("\n")

	lst_all = [] #contains all numbers entered
	lst_odd = [] #contains odd numbers entered
	lst_even = [] #contains even numbers entered

	while True:

		user = input("Enter a number: ")

		if user.upper() == "STOP":
			break
		lst_all.append(user)

	print("\n")
	print("All numbers: " + str(num_all(lst_all)))
	print("Average of all numbers: " + str(average_all(lst_all)))
	print("Sum of all numbers: " + str(sum_all(lst_all)))
	print("\n")
	print("Even numbers: " + str(num_even(lst_all, lst_even)))
	print("Average of even numbers: " + str(average_even(lst_all, lst_odd)))
	print("Sum of even numbers: " + str(sum_even(lst_all, lst_even)))
	print("\n")
	print("Odd numbers: " + str(num_odd(lst_all, lst_odd)))
	print("Average of odd numbers: " + str(average_odd(lst_all, lst_odd)))
	print("Sum of odd numbers: " + str(sum_odd(lst_all, lst_odd)))
	print("\n")
	print("== Program Completed ==")

def num_all(lst_all):
	"""Returns a list of all numbers entered"""
	return list(set(lst_all))

def average_all(lst_all):
	"""Returns the average of all numbers entered by adding 
	the numbers and then dividing by the amount entered"""
	lst_all = [ x for x in map(int, lst_all) ]
	return sum(lst_all) / float(len(lst_all))

def sum_all(lst_all):
	"""Returns the sum of all numbers entered by 
	adding all of the numbers entered"""
	lst_all = [ x for x in map(int, lst_all) ]
	return sum(lst_all)

def num_even(lst_all, lst_even):
	"""Returns a list of all even numbers entered"""
	lst_all = [ x for x in map(int, lst_all) ]
	lst_even = [ x for x in map(int, lst_even) ]

	for i in lst_all:
		if i % 2 or i == 0:
			pass
		else:
			lst_even.append(i)
	return list(set(lst_even))

def average_even(lst_all, lst_even):
	"""Returns the average of all even numbers entered by 
	adding all numbers in lst_even and dividing by the 
	amount of numbers in lst_even"""
	lst_all = [ x for x in map(int, lst_all) ]
	lst_even = [ x for x in map(int, lst_even) ]

	for i in lst_all:
		if i % 2 or i == 0:
			pass
		else:
			lst_even.append(i)
	return sum(lst_even) / float(len(lst_even))

def sum_even(lst_all, lst_even):
	"""Returns the sum of all even numbers entered by 
	adding all numbers in lst_even"""
	lst_all = [ x for x in map(int, lst_all) ]
	lst_even = [ x for x in map(int, lst_even) ]

	for i in lst_all:
		if i % 2 or i == 0:
			pass
		else:
			lst_even.append(i)
	return sum(lst_even)
			
def num_odd(lst_all, lst_odd):
	"""Returns a list of all odd numbers entered"""
	lst_all = [ x for x in map(int, lst_all) ]
	lst_odd = [ x for x in map(int, lst_odd) ]
	for i in lst_all:
		if i % 2 or i == 0:
			lst_odd.append(i)
	return list(set(lst_odd))

def average_odd(lst_all, lst_odd):
	"""Returns the average of all odd numbers entered by 
	adding all numbers in lst_odd and dividing by the 
	amount of numbers in lst_odd"""
	lst_all = [ x for x in map(int, lst_all) ]
	lst_odd = [ x for x in map(int, lst_odd) ]

	for i in lst_all:
		if i % 2 or i == 0:
			lst_odd.append(i)
	return sum(lst_odd) / float(len(lst_odd))

def sum_odd(lst_all, lst_odd):
	"""Returns the sum of all odd numbers entered by 
	adding all numbers in lst_odd"""
	lst_all = [ x for x in map(int, lst_all) ]
	lst_odd = [ x for x in map(int, lst_odd) ]

	for i in lst_all:
		if i % 2 or i == 0:
			lst_odd.append(i)
	return sum(lst_odd)

if __name__ == '__main__':
	main()