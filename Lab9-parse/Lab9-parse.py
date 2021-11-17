# Garrett Thompson
# CSCI 101 Section H
# Python Lab 9
# References: looked up the strip function in order to remove new lines as I could not remember what to use for it
# Time: 45 minutes
punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
               '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
dec_str = ''
with open('Declaration_of_independence.txt', 'r') as dec_file:
    for j in dec_file:
        line_strip = j.strip()
        dec_str += line_strip
        dec_str += ' '
    for i in punctuation:
        dec_str = dec_str.replace(i, '')
    dec_str = dec_str.strip('\n')
    dec_str = dec_str.lower()
    dec_list = dec_str.split(' ')

word_count = 0
unique_word_list = []
print('Would you like to print the number of times a specific word appears OR print the number of words of a specific '
      'length? (1 or 2)')
usr_choice = int(input('CHOICE> '))
if usr_choice == 1:
    print('Enter a word:')
    usr_word = input('WORD> ')
    usr_word_it = usr_word.lower()
    for u in punctuation:
        usr_word_it = usr_word_it.replace(u, '')
    for k in dec_list:
        if k == usr_word_it:
            word_count += 1
        else:
            continue
    print(f'The number of times {usr_word} appears in the document is:')
    print(f'OUTPUT {word_count}')
else:
    print('Enter a length:')
    usr_len = int(input('LENGTH> '))
    for y in dec_list:
        if len(y) == usr_len and y.isalpha():
            if y not in unique_word_list:
                unique_word_list.append(y)
                word_count += 1
            else:
                word_count += 1
        else:
            continue
    print(f'The number of words in the document with length {usr_len} is:')
    print(f'OUTPUT {word_count}')
    print(f'The number of unique words in the document with length 4 is:')
    print(f'OUTPUT {len(unique_word_list)}')
