import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
matrix_list = [
    [7, "", 3],
    ["T","s","i"],
    ["h","%","x"],
    ["i", "" , "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["i", "r", "!"]
]
def decodeMatrix(matrix, items_per_list):
    decoded_words = ""
    i = 0
    while i < items_per_list :
        for char in matrix:
          try :
                if char[i] in alphabet_lower or char[i] in alphabet_upper:
                    decoded_words += char[i]
                else :
                    if decoded_words[-1] == "n"  or char[i] == " ":
                        pass