
for num_a in range (1,11):
    mult_table_num = ""

    for num_b in range(1, 11):
        mult_table_num += f'{num_b * num_a}|'
print(mult_table_num)