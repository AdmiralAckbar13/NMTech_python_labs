#Days.py (Lab 5) [Shane Roeseberg]

import datetime

print("== Days ==")
print("\n")

def main():

	day = int(input("Please enter the day (use the numerical value): "))
	month = int(input("PLease enter the month (use the numerical value): "))
	year = int(input("Please enter the year: "))
	weekday = input("Please enter the weekday (use the alphabetical value): ")

	print("\n")
	print("Date: " + total(day,month,year))
	print("\n")
	print("== Program Exit ==")

def total(day, month, year):
	"""Function uses builtin Python function 'datetime' which is a module that includes 
	functions and classes for doing date and time parsing, formatting, and arithmetic 
	(source: PyMOTW.com), function returns the given day, month and year based on the 
	corresponding numerical value that is input by the user, and returns the weekday 
	based on the corresponding alphabetical value input"""
	date = datetime.date(year, month, day)
	return '{0:%A}, {0:%B} {0:%d}, {0:%Y}' .format(date)

if __name__ == "__main__":
	main()