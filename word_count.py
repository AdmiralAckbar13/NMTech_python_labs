#Word_count.py (lab 6) [Shane Roeseberg]

print("== Word Count ==")
print("\n")
print("------------------------------------------------------------------------------")
print("When entering the filename be sure to include the extension (such as .txt)")
print("------------------------------------------------------------------------------")
print("\n")

def main():
	while True:

		try:
			file = input("Please enter the filename of the file to read: ")
			file_read = open(file, "r")

			user = input("Please enter the word you want to count: ")
			x = 0

			for line in file_read.read().split():
				line = line.strip("!@$%^&*()-_[]\{}|;':,./<>?d\"")

				if line == user:
					x += 1
				else:
					pass

			print("\n")

			if x == 1:
				print("Output: There is" ,(x),  "instance of the word" ,(user), "in the file" ,file,)

			elif x > 1:
				print("Output: There are" ,(x), "instances of the word" ,(user), "in the file" ,file,)

			elif x < 1:
				print("Output: There are" ,(x), "instances of the word" ,(user), "in the file" ,file,)

			print("\n")
			print ("== Program Completed ==")
			file_read.close()
			break

		except IOError:
			print("\n")
			print("------------------------------------------------------------------------------")
			print("The file" ,file, "does not exist, or cannot be found.")
			print("Is it in the same directory as this program?")
			print("Did you include the filename extension?")
			print("------------------------------------------------------------------------------")
			print("\n")

if __name__ == '__main__':
	main()