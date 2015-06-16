#RPN.py (lab 8) [Shane Roeseberg]

import math

def rpn(string):

    array = []

    operators = {"+": lambda x,y: x + y, "-": lambda x,y: x - y, "*": lambda x,y: x * y, "/": lambda x,y: x / y,"sin": lambda y: math.sin(y),"cos": lambda x: math.cos(x)}

    numb = None

    for i in string.split():
        if i in "+-*/":
            x = array.pop()
            y = array.pop()
            numb = operators[i](x,y)
        elif i == "sin":
            numb = operators[i](array.pop())
        elif i == "cos":
            numb = operators[i](array.pop())
        if numb == None:
            array.append((i))
        else:
            array.append(numb)
            
    if len(array) < 1:
        print("Array has more than one item left")
        return 0

    else:
        return array[0]

def main():
    print("== RPN ==")
    print("\n")
    print(rpn(input("Please enter an rpn string: ")))

if __name__ == "__main__":
    main()