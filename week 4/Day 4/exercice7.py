
import random

def get_random_temp(season):

    if season == "winter":
        return(random.randint(-10, 16))
    elif season == "summer":
        return(random.randint(32, 40))
    elif season == "spring":
        return(random.randint(24, 32))
    elif season == "autumn":
        return(random.randint(16, 24))
   
get_random_temp("autumn")

def main():
    temp = get_random_temp("autumn")
    if temp < 0:
        print( "Brrr, that’s freezing! Wear some extra layers today")
    elif 0<= temp <= 16:
        print( "Quite chilly! Don’t forget your coat")
    elif 16< temp <= 23:
         print( "C'EST L'AUTOMNE ESHGHGGGUHVHIC")
    elif 24< temp <= 32:
        print("CHRANAAAA")
    elif 32< temp <= 40:
        print("CANICULEEEE")
main()