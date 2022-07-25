import random

r1=int( input("Choose a number between 1 and 100 : "))
r2 = random.randint(0, 100)

if r1==r2:
    print("You are luckyyyy")
else:
    print("You lost!!!!")
