#type conversion 
a = 2
b = 4.25

sum = a + b # 2.0 + 4.25 => 6.25
print(sum)
#but if we will put 2 in string "" then it will show error bcoz string ko floating values se add krna not allowed
 
 #type casting
a = int("2")  # instead of using int we can use float
b = 4.25
print(a + b)

a = 4.39
a = str(a)
print(type(a))

#input in python 
input("enter your name: ")   #now after running your prog. your can edit your name and then enter it will get saved.

caste = input("enter your caste:")
print("welcome", caste)

name = input("enter name:")
age = int(input("enter age:"))
marks = float(input("enter marks:"))

print("welcome",name)
print("age",age)
print("marks",)
