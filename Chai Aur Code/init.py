# userscore = int(input("Enter your score: "))
# print("Your score is:", userscore)


#question1
# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a child.")
# elif 13 <= age < 20:
#     print("You are a teenager.")
# elif 20 <= age < 60:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")
    
    
#question2
# age = int(input("Enter your age: "))
# day = "Wednesday"

# price = 12 if age >= 18 else 8
# print("the price of the movie ticket is: ", price)  


#question3

# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
# positive_number_count = 0
# for number in numbers:
    # if number > 0:
        # positive_number_count += 1

# print("The count of positive numbers is:", positive_number_count)




#question4
input_string = input("Enter a string: ")
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string
    
print("Reversed string:", reversed_string)
