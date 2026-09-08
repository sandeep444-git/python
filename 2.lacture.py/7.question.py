#WAP to check if a number is a multiple of 7 or not.

number= int(input("enter number:"))
rem = number%7
if (rem == 0):
    print("multiple of 7 ")
else:
    print("not multiple of 7")
