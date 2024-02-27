weight = float(input("Enter your weight :"))
unit = input("(L)bs or (K)kg? :")
if unit == 'l' or unit == 'L':
    print(f"{weight * 0.45} kg")
elif unit == 'K' or 'k':
    print(f"{weight / 0.45} lbs")
else:
    print("Invalid Input!!")