#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 12 - Utility using Git and Incremental Development
#   References:
#   Time: 45 minutes
import math


def load_file(file_name):
    file_content = []
    with open(file_name, 'r') as file:
        temp_content = file.readlines()
        for i in temp_content:
            file_content.append(i.replace('\n', ''))
    return file_content


def update_string(input_str, input_word, index):
    output_string = input_str[0:index] + input_word + input_str[index + 1:]
    print(f'OUTPUT {output_string}')


def find_word_count(list_find, string_find):
    counter = 0
    for i in list_find:
        j = 0
        while j < len(i):
            if i[j:len(string_find) + j] == string_find:
                counter += 1
                j += 1
            else:
                j += 1
    return counter


def score_finder(player_list, score_list, string_find):
    string_find_lower = string_find.lower()
    player_list_final = []
    for i in player_list:
        player_list_final.append(i.lower())
    if string_find in player_list_final:
        player_index = player_list_final.index(string_find_lower)
        print(f'OUTPUT {player_list[player_index]} got a score of {score_list[player_index]}')
    else:
        print(f'OUTPUT player not found')

"""
def union(first_list, second_list):
    union_list = []
    for i in first_list:
        if i not in union_list:
            union_list.append(i)
        else:
            continue
    for i in second_list:
        if i not in union_list:
            union_list.append(i)
        else:
            continue
    return union_list


def intersect(first_list, second_list):
    intersect_list = []
    for i in first_list:
        if i in second_list:
            intersect_list.append(i)
        else:
            continue
    return intersect_list


def not_in(first_list, second_list):
    not_in_list = []
    for i in first_list:
        if i not in second_list:
            not_in_list.append(i)
        else:
            continue
    return not_in_list


def is_prime(number):
    if number == 1:
        return False
    elif number % 2 == 0:
        return True
    iterator = math.sqrt(number)
    iterator = round(iterator)
    for i in range(3, iterator + 1):
        if number % i == 0:
            return False
        else:
            continue
    return True
"""
