#LIST SLICING

marks = [94.3, 65.3, 96.4, 32.6, 69.9]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(len(marks))

student = ["karan", 96.5, 32, "lucknow"]
print(student[0])
student[0] = "arjun"
print(student)

#string slicing mai jaisa hota tha waisa list slicing mai bhi possible h 
 
list = [2, 1, 3]
list.append(4)
print(list)
list.sort( )
print(list)
list.sort( reverse = True )
print(list)
list.reverse()
print(list)
list.insert(3,5)
print(list)

list = [1, 2, 1, 3]
list.pop(0)
print(list)
list.remove(1)
print(list)

tup = (2, 1, 3, 1)
print(tup[0])
print(tup[1])
#tup[0] = 5 this is not possible nhi tuple.

#imp
tup = (1)
print(tup)
print(type(tup))

tup = (1,)
print(tup)
print(type(tup))

tup = (1, 2, 3, 4)
print(tup.index(1))
print(tup.count(1))
