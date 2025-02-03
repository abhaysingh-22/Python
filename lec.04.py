info = {
    "key" : "value",
    "name" : "abhay",
    "learning" : "coding",
    "age" : "35",
}
print(info)
print(type(info))
#list tuple kuch bhi add kr skte ho info mai
#mutable hota h  
print(info["name"]) 
print(info["learning"])
info["name"] = "sony"
info["surname"] = "singh"
print(info)

student = {
    "name" : "abhay singh",
    "subjects" : {
        "physics" : 97,
        "maths" : 89,
        "chem" : 94
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])
print(len(student))

#DICTONARY METHOD

print(list(student.keys()))
print(student.values())
print(student.items())
pairs = (list(student.keys()))
print(pairs[1])

print(student["name"])         #same as below
print(student.get("name"))     #same as above

# print(student["name2"])        #error
print(student.get("name2"))    #no error -->none

new_dict = {"city" : "delhi", "age" : 16}
student.update(new_dict)
print(student)

#SETS

yo = {1, 2, 3, 4, "hello", "abhay"}
print(yo)
print(type(yo))
print(len(yo))   #total number of items

collection = {} #empty dict
collection = set()  #empty set
print(type(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("abhay singh")
 # collection.add([1, 2, 3, 4])     #error since itz a list so it means we are tryign to =add a hasable value
collection.remove(3)
collection.clear()

print(collection )

collection = {"hello", "abhaysingh","jee", "neet"}
print(collection.pop())
print(collection.pop())

set1 = {1, 2, 3, 4}
set2 = {3, 5, 6, 67}
a = set1.union(set2)
b = set1.intersection(set2)

print(a)
print(b)
