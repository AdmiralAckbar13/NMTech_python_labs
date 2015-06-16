def main():
	while True:

 		value = input("Please enter the value you want to charge (type 'stop' to exit): ")

 		if value.upper() == "STOP":
 			print("Stopped!")
 			break

 		value = int(value)

 		if value < 10:
 			
 			print("There are " + str(extra) + " dollars on your calling card. You charged less than $10, so you do not recieve anything extra.")

 		elif value >= 10 and value < 25:
 			
 			print(str(extra_0) + " dollars were added to your calling card.")

 		elif value >= 25 and value < 50:
 			
 			print(str(extra_1) + " dollars were added to your calling card.")

 		elif value >= 50 and value < 100:
 			
 			print(str(extra_2) + " dollars were added to your calling card.")

 		elif value > 100:
 			
 			print(str(extra_3) + " dollars were added to your calling card.")

 		else:
 			print("Invalid input.")

if __name__ == '__main__':
	main()

def call_card():

 	if value < 10:
 		extra = value
 		
 	elif value >= 10 and value < 25:
 		extra_0 = value + 3
 		
 	elif value >= 25 and value < 50:
 		extra_1 = value + 8
 		
 	elif value >= 50 and value < 100:
 		extra_2 = value + 20
 		
 	elif value > 100:
 		extra_3 = value + 25
 		
 	else:
 		print("Invalid input.")

call_card()