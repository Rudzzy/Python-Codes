n = int(input("Enter any Odd number: "))
while n%2 == 0:
    n = int(input("Enter any Odd number Again(other than 1): "))
    print("Try again!!\n")
k = int((n-1)/2)

for i in range (0,k) :
    print("  " * (k-i),end="")
    print("* " * (2*i+1),end="")
    print("  " * (k-i-1),end="")
    print("  " * (k-i),end="")
    print("* " * (2*i+1),end="")
    print("  " * (k-i))

for i in range (1,n+1) :
    print(" " * 2*(i-1),end="")
    print("* " * (2*(n-i)+1),end="")
    print(" " * 2*(i))