#WAP to check if a number entered by the user is odd or even.

number= int(input("enter number:"))
rem = number%2
if (rem == 0):
    print("even")
else:
    print("odd")
