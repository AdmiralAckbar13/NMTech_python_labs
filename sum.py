#Sum.py (Lab 3) [Shane Roeseberg]

def my_sum(n):

    if n <= 1:
        return n

    else:
        return n + my_sum(n - 1)

def main():
	while True:

		print(my_sum(int(input("Please enter a number: "))))

if __name__ =='__main__':
    main()