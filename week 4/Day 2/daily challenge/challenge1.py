a = int(input (" choose a number : "))
b = int(input ("choose a length : "))

numbers = [i * a for i in range(1,b+1)]
print(numbers)