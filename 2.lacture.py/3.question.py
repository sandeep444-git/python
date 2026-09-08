#Grade students based on marks
# marks >= 90, grade = “A”
# 90 > marks >= 80, grade = “B”
# 80 > marks >= 70, grade = “C”
# 70 > marks, grade = “D” Apna College

marks = int (input("inter marks:"))

if (marks >= 90):
    grade = "A"
elif (marks >= 80 and marks <90):
    grade = "B" 
elif (marks >= 70 and marks <80):
    grade = "C" 
elif (marks >= 60 and marks <70):
    grade = "D" 
elif(marks < 60 ):
    grade = "fail"
print("GRADE OF STUDENT :" , grade)
print("END CODE:")

