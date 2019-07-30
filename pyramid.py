# Programmer name: Griffin Cosgrove

# data validation for the amount of rows
numlines = eval(input("Enter an Integer greater than 0 "))
if numlines < 1:
    print("Invalid input")
    numlines = eval(input("Enter an Integer greater than 0"))

# process that creates the number pyramid according to the user input
for x in range(1, numlines + 1):

    for y in range(numlines - x, 0, -1):
        print("    ", end="")

    for y in range(x, 0, -1):
        print(format(y, "4d"), end=" ")

    for y in range(2, x + 1):
        print(format(y, "4d"), end=" ")

    print("")
