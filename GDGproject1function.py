students1 = {
    "name" : "Rahul",
    "m" :int(input("enter math marks of Rahul :")) ,
    "p"  :int(input("enter phy marks of Rahul:")) ,
    "c" :int(input("enter chem marks of Rahul :")) ,
    }
print(students1)
def high_marks(m , p , c):
    if m > p and m > c:
        print("math marks is highest ")
    elif p>m and p>c:
        print("physics marks is highest")
    elif c > m and c>p:
        print("chemistry marks is highest")
    else:
        print("marks are equal or something else")

high_marks(students1["m"] , students1["p"], students1["c"])
def low_marks(m , p , c):
    if m < p and m < c:
        print("math marks is lowest")
    elif p<m and p<c:
        print("physics marks is lowest")
    elif c < m and c<p:
        print("chemistry marks is lowest")
    else:
        print("marks are equal or something else")
low_marks(students1["m"] , students1["p"], students1["c"])
add = students1["m"] + students1["p"]+ students1["c"]
avg = add / (len(students1) - 1)
print("the average marks is ", avg)

def remove_name():
    name = input("Enter the name you wamt to remove : ")
    if students1["name"] == name:
        del students1["name"]
        print(students1)
    else :
        print("the entered name is invalid")
remove_name()

def remove_math():
    marks= int(input("Enter the math marks you wamt to remove : "))
    if students1["m"] == marks:
        del students1["m"]
        print(students1)
   
    else :
        print("the entered marks is invalid")
remove_math()

def remove_phy():
    marks= int(input("Enter the math phy you wamt to remove : "))
    if students1["p"] == marks:
        del students1["p"]
        print(students1)
    else :
        print("the entered marks is invalid")
remove_phy()

def remove_chem():
    marks= int(input("Enter the chem marks you wamt to remove : "))
    if students1["c"] == marks:
        del students1["c"]
        print(students1)
    else :
        print("the entered marks is invalid")
remove_chem()

null_student1 = {}
null_student1["Name"] = input("Enter the student name: ")
null_student1["m"] = int( input("Enter the math marks :"))
null_student1["p"] = int(input("Enter the phy marks:"))
null_student1["c"] = int(input("Enter the chem marks: "))
print(null_student1)

def high_marks(m , p , c):
    if m > p and m > c:
        print("math marks is highest ")
    elif p>m and p>c:
        print("physics marks is highest")
    elif c > m and c>p:
        print("chemistry marks is highest")
    else:
        print("marks are equal or something else")

high_marks(null_student1["m"] , null_student1["p"], null_student1["c"])
def low_marks(m , p , c):
    if m < p and m < c:
        print("math marks is lowest")
    elif p<m and p<c:
        print("physics marks is lowest")
    elif c < m and c<p:
        print("chemistry marks is lowest")
    else:
        print("marks are equal or something else")
low_marks(null_student1["m"] , null_student1["p"], null_student1["c"])
add = null_student1["m"] + null_student1["p"]+ null_student1["c"]
avg = add / (len(null_student1) - 1)
print("the average marks is ", avg)

def remove_name():
    name = input("Enter the name you wamt to remove : ")
    if null_student1["Name"] == name:
        del null_student1["name"]
        print(null_student1)
    else :
        print("the entered name is invalid")
remove_name()

def remove_math():
    marks= int(input("Enter the math marks you wamt to remove : "))
    if null_student1["m"] == marks:
        del null_student1["m"]
        print(null_student1)
   
    else :
        print("the entered marks is invalid")
remove_math()

def remove_phy():
    marks= int(input("Enter the math phy you wamt to remove : "))
    if null_student1["p"] == marks:
        del null_student1["p"]
        print(null_student1)
    else :
        print("the entered marks is invalid")
remove_phy()

def remove_chem():
    marks= int(input("Enter the chem marks you wamt to remove : "))
    if null_student1["c"] == marks:
        del null_student1["c"]
        print(null_student1)
    else :
        print("the entered marks is invalid")
remove_chem()


    
    
