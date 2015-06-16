#Lettercount.py (Lab 5) [Shane Roeseberg]

from collections import Counter

count_dict = {}

print("== Lettercount ==")
print("\n")

def main():

	while True:

		user = input("Enter some letters: ")
		count_dict['user'] = user

		if user == "stop":
			break
		print(counter(user, count_dict))
		print("\n")
		print("== Program Completed ==")

def counter(user, count_dict):
	"""Function uses Python builtin function 'Counter' which is a container 
	that tracks how many times equivalent values are added (source: PyMOTW.com). 
	Function initializes input ('user') to Counter [c = Counter(user)], and then 
	iterates through c, print's the input letters as well as the number of times 
	each letter is input in descending columns"""
	c = Counter(user)
	c.keys()
	for i in c:
		print(i, c[i])
	return counter

if __name__ == '__main__':
	main()