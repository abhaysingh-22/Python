str1 = "yes baba kya haal"
str2 = 'no baba kya haal'
str3 = """yes baba what are you"""

"this is your's body"#here we have used both signle n double quote

str1 = "this is a string.\n we are creating python program"
print(str1)
#next line mai aane k liye .\n dbayen
#tab ka space dene k liye .\t dbayen

str1 = "hello"
str2 = " world"
print(str1 + str2)  #known as concationation

#length in python

str1 = "hello"
len1 = len(str1)
print(len1)

str2 = "world"
len2 = len(str2)
print(len2)

print(str1 + str2)

#INDEX

str = "apan college"
ch = str[0] #from this we will get "a" as outcome similarly when we type str[2]we get "p"
print(ch)
# or we can type print(str[2])

#SLICING

str = "apna college"
print(str[1:4]) #we get "pna"as outcome
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

#if we talk abt negative index then 
str = "apple"
print(str[-3:-1])

#FUNCTIONS

str = "i am studying from bora"
print(str.endswith("ora"))
print(str.endswith("ruhf"))
print(str.capitalize()) #to make 1st letter capital
print(str.replace("o","a"))
print(str.find("o"))
print(str.count("from"))

#CONDITIONAL STATEMENT
#if-elif-else {SYNTAX}
age = 21
if(age >= 18):
    print("can vote and apply for license")
   
num = 5
if(num > 2):
    print("greater than 2")
if(num > 3):
    print("greater than 3")    
    
num = 5
if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")    

light = "pink"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken") 
    
age = 14 
if(age >= 18):
    print("can vote")
else:
    print("cannot vote") 
    
marks = int(input("enter student marks: "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
    
print("grade of the student ->",grade)            
                      
age = int(input("enter the age of person:"))
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")