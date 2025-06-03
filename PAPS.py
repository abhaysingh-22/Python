n = int(input("Enter a number: "))
print("You entered:", n)

with open("practise.txt", "w") as file:
    for i in range(n ):
        line = input(f"Enter line {i+1}: ")
        file.write(line + "\n")