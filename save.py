#Save.py (lab 6) [Shane Roeseberg]

print("== Save ==")
print("\n")
print("--------------------------------------------")
print("Input the filename as 'filename'")
print("Enter an empty field to quit the program.")
print("--------------------------------------------")
print("\n")

def main():

		file_create = input("Enter a file name >> ('file'): ")
		file_write = open(file_create , "a")

		user = input("Input the data to be written to the file: ")

		while (len(user) > 0):
			print(user, file = file_write)
			user = input("Input the data to be written to the file: ")
		print("\n")
		print("== Program Exit ==")
		print("\n")
		print("--------------------------------------------")
		print("Data written to specified filename.")
		print("Check program directory for specified file.")
		print("--------------------------------------------")
		file_write.close()

if __name__ == '__main__':
	main()