#RPN_Calculator.py (Lab 5) [Shane Roeseberg]

print("== RPN Calculator ==")
print("Type 'stop' at any point to exit the program.")
print("\n")

def main():
    while True:

        user = input

        try:
            print(rpn(input("Please enter an RPN string: ")))
        except:
            print("\n")
            print("== Program Exit ==")
            break

def rpn(string):
    """Appends input to stack based on operator used (+-*/)"""
    stack = []
    for i in string.split():
        if i in "+-*/":
            a = stack.pop()
            b = stack.pop()

            if i == "+":
                stack.append(b + a)
            elif i == "-":
                stack.append(b - a)
            elif i == "*":
                stack.append(b * a)
            elif i == "/":
                stack.append(b / a)

        else:
            stack.append(float(i))

    if len(stack) < 1:
        print("The stack has more than one item left")
        return 0
    else:
        return stack[0]

if __name__ == "__main__":
    main()