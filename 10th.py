class student:
     def __init__(self, name):
         self.name = name
         
s1 = student("abhay")
print(s1.name)
del s1.name
# print(s1.name)


class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
acc1 = account("12344", "abcde")

print(acc1.acc_no)
# print(acc1.__acc_pass)


# class person:
#     __name = "crush"
    
# p1 = person()

# print(p1.name)
 
 
class car:
    colour = "balck"
    def start():
        print("car started")
        
    def stop():
        print("car stopped")
        
class ToyotaCar(car):
    def __init__(self, name):
        self.name = name
        
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("raataataa")

print(car1.name)
print(car2.name)
print(car2.colour)

#
class person:
    name = "chomu"
    
    def changename(self, name):
        self.name = name
        
p1 = person()
p1.changename("amol singh")
print(p1.name)
print(person.name)

#
class person:
    name = "chomu"
    
    def changename(self, name):
        person.name = name     #self change to person.
        
p1 = person()
p1.changename("amol singh")
print(p1.name)
print(person.name)

#
class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(99, 98, 27)
print(stu1.percentage)   
#but what if i have to change my phy marks just type
#stu1.phy = 86 but the problem is percent will not change.
##SOLUTION:--








