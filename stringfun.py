#Stringfun.py (Lab 4) [Shane Roeseberg]

def main():
  while True:

    print("== Ends ==")
    print("Type stop at any point to exit the program.")
    print("\n")

    a = input("Enter a string: ")

    if a.upper() == "STOP":
      print("== Program Stopped ==")
      break

    print("Output: " + str(ends(a)))
    print("\n")

    print("== Mix ==")

    a = input("Enter string a: ")

    if a.upper() == "STOP":
      print("== Program Stopped ==")
      break 

    b = input("Enter string b: ")

    if b.upper() == "STOP":
      print("== Program Stopped ==")
      break

    print("Output: " + str(mix(a,b)))
    print("\n")

    print("== Splitit ==")

    a = input("Enter string a: ")

    if a.upper() == "STOP":
      print("== Program Stopped ==")
      break

    b = input("Enter string b: ")

    if b.upper() == "STOP":
      print("== Program Stopped ==")
      break  

    print("Output: " + str(splitit(a,b)))
    print("\n")

def ends(a):

  x = a[:2] + a[-2:]
  return x


def mix(a, b):

  a_2 = b[:2] + a[2:]
  b_2 = a[:2] + b[2:]

  return a_2 + " " + b_2

def splitit(a, b):

  if len(a) % 2 == 0:
    ad = len(a) / 2
    if len(b) % 2 == 0:
      bd = len(b) / 2
    else:
      bd = (len(b) / 2) + 1
  else:
    ad = (len(a) / 2) + 1
    if len(b) % 2 == 0: 
      bd = len(b) / 2
    else:
      bd = (len(b) / 2) + 1
      
  ad = int(ad)
  bd = int(bd)

  return a[:ad] + b[:bd] + a[ad:] + b[bd:]

if __name__ == '__main__':
  main()