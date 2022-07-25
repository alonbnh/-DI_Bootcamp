a = input("which size of the skirt:")
b = input("the text of a message that should be printed on the shirt: ")

def make_shirt():
    if a == "L":
        print("the size of the shirt is " + a + " and the text is: I love python" )
    elif a == "M":
        print("the size of the shirt is " + a + "and the text is: the t-shirt is medium " )
    else:
        print("the text is: the t-shirt is SPECIAL")


make_shirt()