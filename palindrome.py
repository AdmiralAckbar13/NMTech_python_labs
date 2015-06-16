#Palindrome.py (lab 6) [Shane Roeseberg]
#Does not break out of loop

def palindrome():
	while True:
		s_1 = input("Please enter a string: ")
		s_2 = s_1[::-1]

		if s_1 == s_2:
			return ("The word entered IS a palindrome.")
		if s_1 != s_2:
			return ("The word entered IS NOT a palindrome.")

def main():
	print("== Palindrome ==")
	print("\n")

	while True:
		print(palindrome())
		print("\n")

if __name__ == '__main__':
	main()