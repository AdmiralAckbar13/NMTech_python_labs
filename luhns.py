#Luhns.py (Lab 9) [Shane Roeseberg]

def luhn_check(card_number):

    def digits_of(n):
        return [int(d) for d in n.split()]

    digits = digits_of(card_number)
    odd_digits = digits[1::2]
    even_digits = [i + i for i in digits[::2]]
    check = 0

    for i in even_digits:
        if i > 9:
            if i == 10:
                check += 1
            elif i == 12:
                check += 3
            elif i == 14:
                check += 5
            elif i == 16:
                check += 7
            elif i == 18:
                check += 9
        else:
            check += i
    check += sum(odd_digits)
    return check % 10 == 0

def main():

    print("== Luhns ==")
    print("Type stop at any point to exit the program.")
    print("\n")

    while True:
        user = input("Enter a card number: ")

        if user == "stop":
            print("\n")
            print("== Program Exit ==")
            break

        result = luhn_check(user)
        print(str(result))

if __name__ == "__main__":
    main()