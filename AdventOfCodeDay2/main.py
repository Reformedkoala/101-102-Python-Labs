with open('input.txt', 'r') as f:
    num_list = f.readlines()
    new_list = []
    for i in num_list:
        new_list.append(i.replace('\n', ''))

horizontal_tot = 0
depth_tot = 0
aim_tot = 0
for i in new_list:
    if "forward" in i:
        horizontal_tot += int(i[-1])
        depth_tot += aim_tot * int(i[-1])
    elif "down" in i:
        aim_tot += int(i[-1])
    else:
        aim_tot -= int(i[-1])

print(depth_tot * horizontal_tot)