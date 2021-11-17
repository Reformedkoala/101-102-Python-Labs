#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 8 - Lab B - Combing Through a Haystack
#   References:
#   Time: 20 minutes
print('Enter a DNA string s:')
dna_str_s = str(input('s> '))
print('Enter a substring t:')
dna_str_t = str(input('t> '))
i = 0
total_substrings = 0
index_str = ''

if len(dna_str_t) > len(dna_str_s):
    print('Error: Substring is longer than DNA string')
    print('OUTPUT ERROR')
else:
    while i < len(dna_str_s):
        print(i)
        if dna_str_t == dna_str_s[i:len(dna_str_t) + i]:
            index_str += str(i + 1)
            index_str += ' '
            total_substrings += 1
            i += 1
        else:
            i += 1
    print(f'The total number of substrings found is {total_substrings}')
    print(f'OUTPUT {total_substrings}')
    print(f'The locations of these substrings in s are: {index_str}')
    print(f'OUTPUT {index_str}')

