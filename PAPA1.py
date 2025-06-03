n = int(input("Enter a number: "))
print("You entered:", n)

with open("one.txt", "w") as file:
    for i in range(n ):
        line = input(f"Enter line {i+1}: ")
        file.write(line + "\n")
        

with open("one.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
    
    
with open("two.txt", "w") as file:
    file.write(content)