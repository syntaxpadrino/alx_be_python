size = int(input("Enter the size of the pattern: "))

while size < 1 or size > 10:
    print("Size must be between 1 and 10. Please try again.")
    size = int(input("Enter the size of the pattern: "))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print("*", end=" ")
    print()
        