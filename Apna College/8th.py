f = open("sample.txt", "w")
f.close()                      #new file will be created by itself

import os

os.remove("sample.txt")     #the file will get deleted 

# question
## Qa
with open("practise.txt", "w") as f :
    f.write("hi everyone.\nwe are learning english.\nusing Java.\ni like ritika.")
    #f.close() ;-- ye krne se fir file mai changes nhi ho paye ge
## Qb 
with open("practise.txt", "r") as f :
    data = f.read()
    
new_data = data.replace("Java", "Python")
print(new_data)
## Qc
with open("practise.txt", "w") as f:
    f.write(new_data)
    
##Qd
word = "learning"
with open("practise.txt", "r") as f:
    data = f.read()
    if(data.find(word)):
        print("found")
    else:
        print("not found")
##another way of Qd       
def check_for_word():
    word = "learning"
with open("practise.txt", "r") as f:
    data = f.read()
    if(data.find(word)):
        print("found")
    else:
        print("not found")
        
check_for_word()

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                line_no += 1
    return -1
print(check_for_line())

print("hlo world")
         
    
