#  Garrett Thomspon
#  CSCI 101 – Section H
#  Python Lab 11
#  References:
#  Time: 60 miutes
import csv
import os


def read_csv(file_name):
    if file_name[-3:] != 'csv':
        print('OUTPUT Invalid file extension')
    elif os.path.isfile(file_name):
        with open(file_name, 'r', encoding='utf-8') as data_file:
            data_reader = csv.reader(data_file, delimiter=',')
            data_list = []
            for i in data_reader:
                data_list.append(i)
        return data_list
    else:
        print('OUTPUT File does not exist')


rows = read_csv('nc_charlotte_2020_04_01.csv')


def stops_by_race(rows, race):
    for i in rows[0]:
        if i == 'subject_race':
            race_index = rows[0].index(i)
        else:
            continue
    race_counter = 0
    if race == 'ALL':
        return len(rows) - 1
    for i in rows[1:]:
        if i[race_index] == race:
            race_counter += 1
        else:
            continue
    return race_counter


def stops_by_sex(rows, sex):
    for i in rows[0]:
        if i == 'subject_sex':
            sex_index = rows[0].index(i)
        else:
            continue
    sex_counter = 0
    if sex == 'ALL':
        return len(rows) - 1
    for i in rows[1:]:
        if i[sex_index] == sex:
            sex_counter += 1
        else:
            continue
    return sex_counter


print(stops_by_race(rows, 'black'))
