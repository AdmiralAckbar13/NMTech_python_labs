#Navigate2.py (Lab 4) [Shane Roeseberg]

import turtle

stored = []
stored_direction = []

print("== Navigate 2 ==")
print("Type 'stop' at any point to produce output.")
print("\n")

def main():

    while True:

        direction = input("Please enter a direction: ")
        if direction == "forward":
            stored.append(direction)
            amount = int(input("How far forward? "))
            if int(amount) < 0:
                print("Invalid number, not moving")
            stored_direction.append(amount)

        elif direction == "left":
            stored.append(direction)
            degrees = int(input("How many degrees? "))
            if int(degrees) < 0:
                print("Invalid number, not moving.")
            stored_direction.append(degrees)

        elif direction == "right":
            stored.append(direction)
            degrees = int(input("How many degrees? "))
            if int(degrees) < 0:
                print("Invalid number, not moving.")
            stored_direction.append(degrees)

        elif direction == 'stop':

            print("\n")
            print("== Program Completed ==")
            break

        else:
            print("Invalid number, not moving.")

    stored_direction.reverse()

    for direction in stored:
        if direction == "forward":
            turt_forward(stored_direction.pop())
        elif direction == "left":
            turt_left(stored_direction.pop())
        elif direction == "right":
            turt_right(stored_direction.pop())

def turt_forward(amount):
    turtle.forward(amount)

def turt_left(degrees):
    turtle.left(int(degrees))

def turt_right(degrees):
    turtle.right(int(degrees))

if __name__ == '__main__':
    main()