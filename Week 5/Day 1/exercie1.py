

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1= Cat("alon",11)
cat2= Cat("Adam",13)
cat3= Cat("Amecam",14)

def oldest(age1, age2, age3):
    return max(age1, age2, age3)

x = oldest(cat1.age, cat2.age, cat3.age)

print(f'The oldest cat is {x} years old and his name')

