class student:
    name = "abhay"
    
s1 = student()
print(s1.name)

s2 = student()
print(s2.name)

class car:
    colour = "orange"
    brand = "grand vitara"
    
car1 = car()
print(car1.colour)
print(car1.brand)

class student:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database.")
        
s1 = student("ritika")
print(s1.name)

s2 = student("sony")
print(s2.name)

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database.")
        
s1 = student("amol", 89)
print(s1.name, s1.marks)

s2 = student("kabeer", 69)
print(s2.name, s2.marks)

#METHODS
class student:
    def __init__(self, name, marks):
      self.name = name
      self.marks = marks
    
    def welcome(self):
        print("welcome student,", self.name)

s1 = student("karan",50)
s1.welcome()

#QUESTION
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)
        
s1 = student("abhay singh", [99, 43, 65])
s1.get_avg()

s1.name = "ironman"    #way to change the name directly 
s1.get_avg()

        
    