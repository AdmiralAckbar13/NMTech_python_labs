#Sorted.py (Lab 4) [Shane Roeseberg]

def main():

	print("== Sorted ==")
	print("Type 'stop' at any point to produce output and exit the program.")
	print("\n")

	lst = []
	lst_2 = []

	while True:

		user = input("Enter a number: ")

		if user.upper() == "STOP":
			break
		lst.append(user)
	print("Output: " + str(ascend(lst)))
	print("\n")
	print("== Program Completed ==")

def ascend(lst):
	"""Returns a list in ascending order without duplicate numbers"""
	for i in range(len(lst)):
		for x in range(len(lst) - 1):
			if lst[x] > lst[x + 1]:
				lst[x + 1], lst[x] = lst[x], lst[x + 1]

	# return list(set(lst)) list(set(target lst)) removes duplicates but breaks order?
	return lst

if __name__ == '__main__':
	main()