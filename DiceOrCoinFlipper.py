import random

Choice = input("Dice(d) or Coin(c) : ").lower()

if  Choice == 'd' :
    while True:
        Value = input(">")
        if Value == "" : print(f'>{random.randint(1,6)}')
        else: break

elif Choice == 'c' :
    while True:
        Value = input(">")
        FlipperValue= random.randint(1,2)
        if FlipperValue== 1 : k = 'H'
        else : k = 'T'
        if Value == "" : print(f'>{k}')
        else : break

else : print("Invalid Input!!")