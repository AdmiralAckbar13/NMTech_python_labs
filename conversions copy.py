#Conversions.py (Lab 1) [Shane Roeseberg]

def main():
	while True:

		celsius = input("Please input a temperature in Celsius (type 'stop' to stop): ") #Get input from user.
		
		if celsius.upper() == "STOP":
			print ("Stopped!")
			break

		celsius = float(celsius) #Make sure it is stored as a number with decimal point.

		kelvin = celsius + 273.15 #Perform conversion to Kelvin.

		print('Kelvin temperature: ' + str(kelvin)) #Display converted Kelvin value.

		fahrenheit = 9.0/5.0 * celsius + 32 #Perform conversion to Fahrenheit.

		print('Fahrenheit temperature: ' + str(fahrenheit)) #Display converted Fahrenheit value.

if __name__ == '__main__':
	main()