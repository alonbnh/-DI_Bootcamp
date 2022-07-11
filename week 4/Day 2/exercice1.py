my_fav_numbers = [1,2,3]
my_fav_numbers.append(12)
my_fav_numbers.append(10)
my_fav_numbers.pop(-1)
print(my_fav_numbers)

friend_fav_numbers=[7, 8, 9]

our_fav_numbers = [*my_fav_numbers, *friend_fav_numbers]
print(our_fav_numbers)