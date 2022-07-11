def Convert(string):
    li = list(string.split(" "))
    return li

b = input("What's your favorite fruits please separate them with a space:")
print(Convert(b))

c = input("chose another fruit! ")
if c in b:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")