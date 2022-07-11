string_question=input('whats is ur best food and why ?')
if len(string_question)< 10:
    print("string not long enough")
elif len(string_question) > 10:
    print("string too long")
print(string_question[0])
print(string_question[-1])
length = len(string_question)
for row in range(length):
 for col in range(row+1):
    print (string_question[col]),
    print