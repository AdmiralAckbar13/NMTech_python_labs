#Conversions.py (Lab 2) [Shane Roeseberg]

def main():
	while True:

		celsius = input("Please input a temperature in Celsius (type 'stop' to stop): ")

		if celsius.upper() == "STOP":
			print("Stopped!")
			break

		user = input("Please choose Kelvin (K) or Fahrenheit (F) or type 'stop' to stop: ")

		if user.upper() == "STOP":
			print("Stopped!")
			break

		celsius = float(celsius) #Make sure it is stored as a number with decimal point.

		kelvin = celsius + 273.15 #Conversion to Kelvin.
		fahrenheit = 9.0/5.0 * celsius + 32 #Conversion to Fahrenheit.

		if user == "K":
			print("You chose Kelvin.")
		elif user == "F":
			print("You chose Fahrenheit")
		else:
			print("You entered a letter I do not recognize.  Please choose Kelvin (K) or Fahrenheit (F)")

		if user == "K":
			print('Kelvin temperature: ' + str(kelvin)) #If user input = "K" display converted Kelvin value.

		if user == "F":
			print('Fahrenheit temperature: ' + str(fahrenheit)) #If user input = "F" display converted Fahrenheit value.

if __name__ == '__main__':
	main()