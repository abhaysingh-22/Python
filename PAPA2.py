file = open("one.txt", "r")

# Tell the current position
print("Current position:", file.tell())

# Read 5 characters
print("Reading:", file.read(5))

# Tell the position after reading
print("New position:", file.tell())

# Move pointer back to beginning
file.seek(0)

# Read again
print("After seek():", file.read(5))
print("After seek():", file.tell())



file.close()
