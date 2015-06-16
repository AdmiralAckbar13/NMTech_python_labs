#Fractions.py (Lab 4) [Shane Roeseberg]

def main():

	while True:

		frac_lst = []

		print("== Fractions ==")
		print("\n")
		print("== Multiplication and Division ==")

		fraction = input("Enter a fraction: ")
		fraction = tuple(map(int, fraction.split('/')))
		fraction_2 = input("Enter a fraction: ")
		fraction_2 = tuple(map(int, fraction_2.split('/')))

		multiply = frac_multiply(fraction,fraction_2)
		divide = frac_divide(fraction, fraction_2) 

		print("Multiplication of the fractions:", multiply[0],"/",multiply[1])
		print("Division of the first fraction by the second fraction:", divide[0],"/",divide[1])  
		print("\n")
		print("== Smallest Fraction ==")

		break
		continue

	while True:

		fraction_3 = input("Enter a fraction: ")

		if fraction_3.upper() == "STOP":
			break
		fraction_3 = tuple(map(int, fraction_3.split('/')))	
		frac_lst.append(fraction_3)

		smallest = ascend(frac_lst)

	print("The smallest fraction is:", smallest[0],"/",smallest[1]) 
	print("\n")
	print("== Program Completed ==")

def frac_multiply(fraction,fraction_2):
	"""Returns the multiplication of two fractions. Multiplies the 
	numerator of both fractions and the denominator of both fractions."""
	numer = fraction[0] * fraction_2[0]
	denom = fraction[1] * fraction_2[1]
	result = (numer, denom)
	return result

def frac_divide(fraction, fraction_2):
	"""Returns the division of two fractions. Multiplies the 
	reciprocal of the divisor"""
	numer = fraction[0] * fraction_2[1]
	denom = fraction[1] * fraction_2[0]
	result = (numer, denom)
	return result

def ascend(frac_lst):
	"""Returns the smallest fraction.  Sorts inputs from smallest 
	to largest and returns the smallest (1st) item in the list"""
	for i in range(len(frac_lst)):
		for x in range(len(frac_lst) -1):
			if frac_lst[x] > frac_lst[x + 1]:
				frac_lst[x + 1], frac_lst[x] = frac_lst[x], frac_lst[x + 1]

	return frac_lst[0]
	
if __name__ == '__main__':
	main()