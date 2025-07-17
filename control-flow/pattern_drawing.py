#input a positive integer
positive_integer = int(input("Enter the size of the pattern:"))

rows = 0   # start at row 0

while rows < positive_integer:
    for columns in range(positive_integer):
        print("*", end="") # print stars on the same line
        print()    # moves to the next line
        rows += 1

