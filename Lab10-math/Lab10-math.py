#  Garrett Thompson
#  CSCI 101 – Section A
#  Python Lab 10
#  References:
#  Time: 45 minutes
import csv
print('Enter the name of the file containing the math problems.')
math_file = input('MATHFILE> ')
print('Enter the name of the file in which to store the results.')
result_file = input('OUTPUTFILE> ')
with open(math_file, 'r') as math:
    math_reader = csv.reader(math, delimiter=',')
    math_list = []
    final_list = []
    for i in math_reader:
        math_list.append(i)
    with open(result_file, 'w', newline='') as results:
        i = 0
        results_writer = csv.writer(results, delimiter=',')
        for j in math_list:
            while len(j) != 1:
                print(j[i])
                temp_sum = 0
                if j[i] == '-':
                    temp_sum = float(j[i-1]) - float(j[i+1])
                    j.insert(0, temp_sum)
                    j.pop(i)
                    j.pop(i)
                    j.pop(i)
                    i = 0
                elif j[i] == '+':
                    temp_sum = float(j[i-1]) + float(j[i+1])
                    j.insert(0, temp_sum)
                    j.pop(i)
                    j.pop(i)
                    j.pop(i)
                    i = 0
                elif j[i] == '*':
                    temp_sum = float(j[i-1]) * float(j[i+1])
                    j.insert(0, temp_sum)
                    j.pop(i)
                    j.pop(i)
                    j.pop(i)
                    i = 0
                elif j[i] == '/':
                    temp_sum = float(j[i-1]) / float(j[i+1])
                    j.insert(0, temp_sum)
                    j.pop(i)
                    j.pop(i)
                    j.pop(i)
                    i = 0
                else:
                    i += 1
        for i in math_list:
            for j in i:
                final_list.append(round(float(j)))
        results_writer.writerow(final_list)
