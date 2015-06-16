#Fractions2.py (lab 8) [Shane Roeseberg]

import functools
import string

def prompt_fractions():
	fraction = ""
	listof_fractions = []
	first_numb = ""
	second_number = ""

	while fraction != "stop":
		fraction = input("Please enter a fraction: ")
		if fraction != "stop":
			listof_fractions.append(tuple(map(int,fraction.split("/"))))
	return listof_fractions

def min_frac(global_x, new):
		global_decimal = global_x[0] / global_x[1]
		new_decimal = new[0] / new[1]

		if global_decimal < new_decimal:
			return global_x
		else:
			return new

def sum_frac(global_x, new):
    return ((global_x[0] * new[1]) + (new[0] * global_x[1]), global_x[1] * new[1])

def reduce_fraction(global_x):
	num = global_x[0]
	denom = global_x[1]

	while num:
		num, denom = denom % num, num
	return(int(global_x[0] / denom) , int(global_x[1] / denom))

def reduced(fraction):
	if fraction == reduce_fraction(fraction):
		return True
	else:
		return False

def sort_fraction(fraction_list):
	fraction_list = sorted(fraction_list, key = lambda x: x[0] / x[1])
	return fraction_list

def main():

	print("== fractions 2 ==")
	print("Type 'stop' at any point to produce output.")
	print("Enter fractions i.e. 4/5, 2/3 etc.")
	print("\n")

	while True:

		float_to_frac = []
		lowest_frac = []
		sorted_list = []

		listof_fractions = prompt_fractions()

		format_frac = lambda fraction_x: "{}/{}".format(fraction_x[0],fraction_x[1])

		smallest = functools.reduce(min_frac, listof_fractions)
		print("\n")
		print("Smallest fraction:", format_frac(smallest))

		sumfrac = functools.reduce(sum_frac, listof_fractions)
		print("Sum of fractions:", format_frac(sumfrac))

		reducedfrac = list(map(reduce_fraction, listof_fractions))
		for i in reducedfrac:
			float_to_frac.append(format_frac(i))
		print("Reduced fractions:", (", ".join(float_to_frac)))

		almost_lowest_frac = list(filter(reduced, listof_fractions))
		for i in almost_lowest_frac:
			lowest_frac.append(format_frac(i))
		print("Already reduced fractions:", (", ".join(lowest_frac)))

		fracsorted = sort_fraction(listof_fractions)

		for i in fracsorted:
			sorted_list.append(format_frac(i))
		fracsorted = sorted_list
		
		print("Sorted fractions:", (", ".join(fracsorted)))
		print("\n")

if __name__ == "__main__":
	main()