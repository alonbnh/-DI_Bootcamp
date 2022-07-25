


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# age = family.values()
age = family.items()

payment = []

for name,age in family.items():
    price = 0
    if 3 < age < 12:
        price = 10
        
    elif age > 12 :
        price = 15
        
    payment.append[(name, price)]


print(payment.append[(name, price)])