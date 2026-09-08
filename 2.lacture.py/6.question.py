#WAP to find the greatest of 3 numbers entered by the user.


a = int (input("enter first number:"))
b = int (input("enter second number:"))
c = int (input("enter third  number:"))

if (a>=b and a>c):
    print("first greatest number:" ,a )
elif (b>=a and b>c):
     print("second greatest number:" ,b )
else :
      print("third greatest number:" ,c )