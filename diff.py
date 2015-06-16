#Diff.py (lab 6) [Shane Roeseberg]

print("== Diff ==")
print("\n")
print("------------------------------------------------------------------------------")
print("When entering the filename be sure to include the extension (such as .txt)")
print("Type 'stop' at any point to exit the program.")
print("------------------------------------------------------------------------------")
print("\n")

def diff_lines_1(lst, lst_2):
	"""Takes lines of both files (which have been put into respective lists) 
	and gets the differences in lst_2, creates a new list of the differences, 
	then formats the list of differences into seperate lines"""

	z = set(lst_2)
	lst_3 = [i for i in lst if i not in z] #pulls differences between both lists.
	format_output = '\n'.join([str(e) for e in lst_3]) #format list of differences into lines.
	return format_output

def diff_lines_2(lst, lst_2):
	"""Takes lines of both files (which have been put into respective lists) 
	and gets the difference in lst, creates a new list of the differences, 
	then formats the list of differences into seperate lines"""

	y = set(lst)
	lst_4 = [i for i in lst_2 if i not in y]
	format_output_2 = '\n'.join([str(c) for c in lst_4])
	return format_output_2

def main():
	while True:

		try:
			user_1 = input("Please enter the filename 1: ")

			if user_1 == "stop":
				print("\n")
				print("== Program Exit ==")
				break

			user_2 = input("Please enter the filename 2: ")

			if user_2 == "stop":
				print("\n")
				print("== Program Exit ==")
				break

			file_1 = open(user_1, "r")
			lst = file_1.readlines() #put lines in text file into list.
			file_2 = open(user_2, "r")
			lst_2 = file_2.readlines() #put lines in text file into list.

			print("\n")
			print("Output: ")
			print(diff_lines_1(lst, lst_2))
			print(diff_lines_2(lst, lst_2))

		except IOError:
			print("\n")
			print("------------------------------------------------------------------------------")
			print("The file" ,user_1, "and/or" ,user_2, "does not exist, or cannot be found.")
			print("Are the file(s) in the same directory as this program?")
			print("Did you include the filename extension?")
			print("------------------------------------------------------------------------------")
			print("\n")

if __name__ == '__main__':
	main()