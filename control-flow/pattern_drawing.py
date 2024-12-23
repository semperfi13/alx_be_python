size = int(input("Enter the size of the pattern: "))

while size > 0:
    for i in range(1, 5):
        print("*", end="")
    print()
    size = size - 1
