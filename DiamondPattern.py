n = int(input("Enter a Number: "))
for i in range (1,n) :
    print(" " * (n-i-1),end="")
    print("* " * (i),end="")
    print(" " * (n-i))

for i in range (2,n) :
    print(" " * (i-1), end="")
    print("* " * (n-i), end="")
    print(" " * (i-1))

