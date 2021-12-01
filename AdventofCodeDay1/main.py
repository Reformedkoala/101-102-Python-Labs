with open('input.txt', 'r') as f:
    num_list = f.readlines()
    new_list = []
    for i in num_list:
        new_list.append(i.replace('\n', ''))

j = 0
sum_list = []
while j < len(new_list)-2:
    cur_sum = int(new_list[j]) + int(new_list[j + 1]) + int(new_list[j + 2])
    sum_list.append(cur_sum)
    j += 1

i = 0
value_list = []
while i < len(sum_list):
    if i == 0:
        i += 1
    elif int(sum_list[i]) > int(sum_list[i-1]):
        value_list.append('increased')
        i += 1
    elif int(sum_list[i]) < int(sum_list[i-1]):
        value_list.append('decreased')
        i += 1
    else:
        i += 1
print(value_list.count('increased'))
