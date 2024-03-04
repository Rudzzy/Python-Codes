n = int(input("Enter a Number: "))
for i in range (1,n) :
    print("*" * (i-1), end="")
    print("  " * (n-i), end="")
    print("*" * (i-1))

for i in range (3,n) :
    print("*" * (n-i),end="")
    print("  " * (i-1),end="")
    print("*" * (n-i))