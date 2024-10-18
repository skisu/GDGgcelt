students1 = {
    "name" : "Rahul",
    "math" :int(input("enter math marks of Rahul :")) ,
    "phy"  :int(input("enter phy marks of Rahul:")) ,
    "chem" :int(input("enter chem marks of Rahul :")) ,
    }

print(students1)
add = students1["math"] +  students1["phy"]+ students1["chem"]
avg = add / (len(students1) - 1)
print("The avg marks is : " ,avg)
if(students1["math"] > students1["phy"] and students1["math"] > students1["chem"]):
  print("Math marks is greatest")
elif(students1["phy"] > students1["math"]  and students1["phy"] >  students1["chem"]):
  print("Physics marks is greatest")
else:
  print("Chemistry marks is greatest")
if(students1["math"] < students1["phy"] and students1["math"] < students1["chem"]):
  print("Math marks is lowest")
elif(students1["phy"] < students1["math"] and students1["phy"] < students1["chem"]):
  print("Physics marks is lowest")
else:
  print("Chemistry marks is lowest")
name = input("Enter the name :")
if students1["name"] == name:
    del students1["name"]
    print(students1)
else:
 print("Entered name is invalid")
math = int(input("Enter the proper math marks :"))
if students1["math"] == math:
    del students1["math"]
    print(students1)
else:
 print("Entered marks is invalid")
phy = int(input("Enter the proper phy marks :"))
if students1["phy"] == phy:
    del students1["phy"]
    print(students1)
else:
 print("Entered marks is invalid")
chem = int(input("Enter the proper chem marks :"))
if students1["chem"] == chem:
    del students1["chem"]
    print(students1)
else:
 print("Entered marks is invalid")
students2 = {
        "name" : "Shubham",
         "math" :int(input("enter math marks of Shubham :")) ,
         "phy"  :int(input("enter phy marks of Shubham:")) ,
         "chem" :int(input("enter chem marks of Shubham :")) ,
            }
print(students2)
add = students2["math"] +  students2["phy"]+ students2["chem"]
avg = add / (len(students1) - 1)
print("The avg marks is : " ,avg)
if(students2["math"] > students2["phy"]  and students2["math"] > students2["chem"]):
  print("Math marks is greatest")
elif(students2["phy"] > students2["math"] and students2["phy"] > students2["chem"]):
  print("Physics marks is greatest")
else:
  print("Chemistry marks is greatest")
if(students2["math"] < students2["phy"]  and students2["math"] < students2["chem"]):
  print("Math marks is lowest")
elif(students2["phy"] < students2["math"]  and students2["phy"]  < students2["chem"]):
  print("Physics marks is lowest")
else:
  print("Chemistry marks is lowest")
name = input("Enter the name :")
if students2["name"] == name:
    del students2["name"]
    print(students2)
else:
 print("Entered name is invalid")
math = int(input("Enter the proper math marks :"))
if students2["math"] == math:
    del students2["math"]
    print(students2)
else:
 print("Entered marks is invalid")
phy = int(input("Enter the proper phy marks :"))
if students2["phy"] == phy:
    del students2["phy"]
    print(students2)
else:
 print("Entered marks is invalid")
chem = int(input("Enter the proper chem marks :"))
if students2["chem"] == chem:
    del students2["chem"]
    print(students2)
else:
 print("Entered marks is invalid")

  
null_student1 = {}
null_student1["Name"] = input("Enter the student name: ")
null_student1["math"] = int( input("Enter the math marks :"))
null_student1["phy"] = int(input("Enter the phy marks:"))
null_student1["chem"] = int(input("Enter the chem marks: "))
print(null_student1)
add = null_student1["math"] +  null_student1["phy"]+ null_student1["chem"]
avg = add / (len(null_student1) - 1)
print("The avg marks is : " ,avg)
if(null_student1["math"] > null_student1["phy"]  and null_student1["math"]  > null_student1["chem"]):
  print("Math marks is greatest")
elif(null_student1["phy"] > null_student1["math"] and null_student1["phy"] > null_student1["chem"]):
  print("Physics marks is greatest")
else:
  print("Chemistry marks is greatest")
if(null_student1["math"] < null_student1["phy"]  and  null_student1["math"] < null_student1["chem"]):
  print("Math marks is lowest")
elif(null_student1["phy"] < null_student1["math"] and null_student1["phy"] < null_student1["chem"]):
  print("Physics marks is lowest")
else:
  print("Chemistry marks is lowest")
name = input("Enter the name :")
if null_student1["Name"] == name:
    del null_student1["Name"]
    print(null_student1)
else:
 print("Entered name is invalid")
math = int(input("Enter the proper math marks :"))
if null_student1["math"] == math:
    del null_student1["math"]
    print(null_student1)
else:
 print("Entered marks is invalid")
phy = int(input("Enter the proper phy marks :"))
if null_student1["phy"] == phy:
    del null_student1["phy"]
    print(null_student1)
else:
 print("Entered marks is invalid")
chem = int(input("Enter the proper chem marks :"))
if null_student1["chem"] == chem:
    del null_student1["chem"]
    print(null_student1)
else:
 print("Entered marks is invalid")

null_student2 = {}
null_student2["Name"] = input("Enter the student name :")
null_student2["math"]  = int( input("Enter the math marks : "))
null_student2["phy"] = int(input("Enter the phy marks:"))
null_student2["chem"] = int(input("Enter the chem marks :"))
print(null_student2)
add = null_student2["math"] +  null_student2["phy"]+ null_student2["chem"]
avg = add / (len(null_student1) - 1)
print("The avg marks is : " ,avg)
if(null_student2["math"] > null_student2["phy"]  and null_student2["math"]  > null_student2["chem"]):
  print("Math marks is greatest")
elif(null_student2["phy"] > null_student2["math"] and null_student2["phy"] > null_student2["chem"]):
  print("Physics marks is greatest")
else:
  print("Chemistry marks is greatest")
if(null_student2["math"] < null_student2["phy"]  and  null_student2["math"] < null_student2["chem"]):
  print("Math marks is lowest")
elif(null_student2["phy"] < null_student2["math"] and null_student2["phy"] < null_student2["chem"]):
  print("Physics marks is lowest")
else:
  print("Chemistry marks is lowest")
name = input("Enter the name :")
if null_student2["Name"] == name:
    del null_student2["Name"]
    print(null_student2)
else:
 print("Entered name is invalid")
math = int(input("Enter the proper math marks :"))
if null_student2["math"] == math:
    del null_student2["math"]
    print(null_student2)
else:
 print("Entered marks is invalid")
phy = int(input("Enter the proper phy marks :"))
if null_student2["phy"] == phy:
    del null_student2["phy"]
    print(null_student2)
else:
 print("Entered marks is invalid")
chem = int(input("Enter the proper chem marks :"))
if null_student2["chem"] == chem:
    del null_student2["chem"]
    print(null_student2)
else:
 print("Entered marks is invalid")
