# def say_hello():
#     """A function that says hello"""
#     print("Hello!") 

# say_hello()

# def say_hello(username):
#     print("Hello "+username)

# say_hello("Rick") # "Rick" is an argument
# # output "Hello Rick"

# say_hello("Morty") # "Morty" is an argument
# # output "Hello Morty"

# def say_hello(username, language):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello("Rick", "FR")

# def calculation(a, b):
#     print(a+b,a-b)
# res = calculation(40, 10)

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)

# def divide_by_three(number):
#   return number / 3

# first_number = 12
# first_number_computed = divide_by_three(first_number)
# print(first_number_computed)


# second_number = 27
# second_number_computed = divide_by_three(second_number)
# print(second_number_computed)


# my_tuple = ("jimi", "hendrix")
# first_name, last_name = my_tuple
# print("First name is: " + first_name)
# print("Last name is: " + last_name)


# def format_name(first_name, last_name):
#     return (first_name.title(), last_name.title())

# first, last = format_name("RICk", "mORTY")
# print(first)
# print(last)



# def greet_users(users):             # users should be a list
#     for user in users:              # Because it's a list, we can loop through it
#         print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

# usernames = ["steve", "stan", "debbie"]
# greet_users(usernames)