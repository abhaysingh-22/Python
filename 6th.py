count = 1    #known as iterators
while count <= 5 :     #iteration
    print("hello")
    count += 1
print(count)    

#thoda tough h smjna ye jo uper likha h but dyan se krna smj aa jaye ga 

#print numbers from 1 to 5

i = 1
while i <= 5 :
    print(i)
    i += 1
    
i = 5
while i >= 1 :
    print(i)
    i -= 5
    
# print numbers from 1 to 100 
i = 1
while i <=100 :
    i += 1
    print(i)
    
#print number from 100 to 1
i = 100
while i >= 1 :
    i -= 1
    print(i)
  
#ques.3  
i = 1
while i <= 10:
    print(3*i)
    i += 1
    
# i = 1
# n = int(input("enter the number: "))
# while i <= 10:
#     print(n*i)
#     i += 1 
    
#ques 4
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#known as traverse
idx = 0
while idx < len(nums) :
    print(nums[idx])  #nums[0], nums[1], nums[2]...
    idx += 1
    
#que5
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x =36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
    else:
        print("finding")
    i += 1
    
#BREAK AND COUTINUE

i = 1
while i <= 5 :
    print(i)
    if(i == 3):
        break
    i += 1
    
print("end of loop")

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x =36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        break
    else:
        print("finding")
    i += 1
    
print("end of loop")

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue  #acts as skip 
    print(i)
    i += 1
print("end here")
    
i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1
print("end here")

i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
print("end here")


nums = [1, 2, 3, 4]

for val in nums:
    print(val)
    
    
a = ["hi", "abhay", "ritika"]
for el in a:
    print(el)
     
     
a  = "abhay"
for char in a:
    print(char)   #character
else:
    print("end")

a = "abhay"
for char in a:
    if(char == 'h'):
        print("h found")   #character
        break
    print(char)
else:
    print("end")

#question
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in list:
    print(el)
    
#question
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

idx = 0
for el in tup:
    if(el == x):
        print("number found at idx", idx)
    idx += 1
print("loop ended here")
    
    
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

idx = 0
for el in tup:
    if(el == x):
        print("number found at idx", idx)
        break
    idx += 1
    
#RNAGE

print(range(5))

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
#alt. method 
for i in seq:
    print(i)
    
for i in range(2, 10, 2):
    print(i)
    
for i in range(100, 0, -1):
    print(i)
    
    
n = 5
for i in range(1, 11):
    print(n*i)
    
#PASS STATEMENT
for i in range(5):
    pass

if i > 5:
    pass
print("hi abhay how are you")