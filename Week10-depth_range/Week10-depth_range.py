#  Garrett Thompson
#  CSCI 102 – Section A
#  Week 10 Lab
#  References:
#  Time: 60 minutes
import csv
with open('formations.csv', 'r') as formations:
    formations_reader = csv.reader(formations, delimiter=',')
    formations_list = []
    depth_list = []
    formation_list = []
    final_list = []
    j = 0
    for i in formations_reader:
        formations_list.append(i)
    formations_list.pop(0)
    for i in formations_list:
        formation_list.append(i[1])
        depth_list.append(i[0])
    with open('formations_parsed.csv', 'w', newline='') as parse:
        parse_writer = csv.writer(parse, delimiter=',')
        parse_writer.writerow(['Depth', 'Start Depth', 'End Depth', 'Difference in Depth', 'Formation'])
        while j < len(formations_list):
            temp_list = []
            temp_list.append(depth_list[j])
            depth_str = depth_list[j]
            depth_temp = depth_str.split('-')
            temp_list.append(float(depth_temp[0]))
            temp_list.append(float(depth_temp[1]))
            depth_diff = float(depth_temp[1]) - float(depth_temp[0])
            depth_diff = f'{depth_diff:.2f}'
            temp_list.append(depth_diff)
            temp_list.append(formation_list[j])
            final_list.append(temp_list)
            j += 1
        for i in final_list:
            parse_writer.writerow(i)
