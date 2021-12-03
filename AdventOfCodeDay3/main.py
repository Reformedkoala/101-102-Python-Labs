with open('input.txt', 'r') as f:
    num_list = f.readlines()
    new_list = []
    for i in num_list:
        new_list.append(i.replace('\n', ''))

data_list = new_list
j = 0
gamma_counter = ''
epsilon_counter = ''
while j < len(data_list[0]):
    bit_one = 0
    bit_zero = 0
    length = len(data_list)
    for i in data_list:
        if i[j] == '1':
            bit_one += 1
        else:
            bit_zero += 1
    if bit_one > bit_zero:
        for k in range(length):
            if data_list[k][j] != '1':
                data_list.append(data_list[k])
            else:
                continue
    elif bit_zero == bit_one:
        for k in range(length):
            if data_list[k][j] != '1':
                data_list.append(data_list[k])
            else:
                continue
    else:
        for y in range(length):
            if data_list[y][j] == '1':
                data_list.append(data_list[y])
            else:
                continue
    for u in range(length):
        data_list.pop(0)
    if len(data_list) == 1:
        print(data_list)
        break
    j += 1
print(data_list)
