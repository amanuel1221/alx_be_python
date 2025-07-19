length = int(input("Enter the size of the pattern: "))
i = 1
while i <= length:
    for j in range(length):
        print("*", end="")
    print()
    i += 1