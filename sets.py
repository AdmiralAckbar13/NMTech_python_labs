#Sets.py (Lab 4) [Shane Roeseberg]

def main():
	
	print("== Sets ==")
	print("Type 'stop' at any point to produce output, move onto list 2 and exit the program.")
	print("\n")
	print("List 1")

	lst = []
	lst_2 = []

	while True:

		user = input("Enter a number: ")
		
		if user.upper() == "STOP":
			break
		lst.append(user)
	print("List 1 is: " + str(lst))
	print("Moving onto list 2")
	print("\n")
	print("List 2")
			
	while True:

		user_1 = input("Enter a number: ")

		if user_1.upper() == "STOP":
			break
		lst_2.append(user_1)
	print("List 2 is: " + str(lst_2))
	print("\n")
	print("The overlap is: " + str(overlap(lst, lst_2)))
	print("The join is: " + str(join(lst, lst_2)))
	print("\n")
	print("== Program Completed ==")

def overlap(lst, lst_2):
	return list(set(lst) & set(lst_2))

def join(lst, lst_2):
	return lst + list(set(lst_2) - set(lst))

if __name__ == '__main__':
	main()