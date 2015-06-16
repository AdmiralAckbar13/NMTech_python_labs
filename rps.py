#rps.py (lab 2) [Shane Roeseberg]

def main():
	
	while True:

		user = input("Enter R, P, or S: ").lower()
		
		if user == "r":
			print("You chose rock (exiting)")
			break

		elif user == "p":
			print("You chose paper (exiting)")
			break

		elif user == "s":
			print("You chose scizzors (exiting)")
			break

		else:
			print("You did not enter R, P, or S. Please try again")
			pass

if __name__ =='__main__':
	main()