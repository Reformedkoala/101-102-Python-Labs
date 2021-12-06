#  Garrett Thompson
#  CSCI 102 – Section A
#  Week 13 Review Lab
#  References:
#  Time: 75 minutes

def decrypt_guess(msg, dic_input):
    msg = msg.split()
    largest_word = max(msg, key=len)
    for y in dic_input:
        if y == largest_word.lower():
            return 1
        else:
            continue
    return 0


with open('dictionary.txt', 'r') as f:
    num_list = f.readlines()
    dic_list = []
    for i in num_list:
        dic_list.append(i.replace('\n', ''))

print('Input the message to encrypt and the desired shift.')
message = input('MESSAGE> ')
shift = int(input('SHIFT> '))
print(f'Your message encrypted with shift {shift}:')
shift %= 26
encrypted_msg = ''
for i in message:
    if i.isalpha() and i.isupper():
        if ord(i) + shift <= 90:
            temp_letter = ord(i)
            temp_letter += shift
            encrypted_msg += chr(temp_letter)
        else:
            temp_letter = ord(i)
            temp_letter += shift
            temp_letter -= 91
            temp_letter += 65
            encrypted_msg += chr(temp_letter)
    elif i.isalpha() and i.islower():
        if ord(i) + shift <= 122:
            temp_letter = ord(i)
            temp_letter += shift
            encrypted_msg += chr(temp_letter)
        else:
            temp_letter = ord(i)
            temp_letter += shift
            temp_letter -= 123
            temp_letter += 97
            encrypted_msg += chr(temp_letter)
    else:
        encrypted_msg += i
print(f'OUTPUT {encrypted_msg}')

print('Input the message to decrypt using brute force')
decrypt_message = input('MESSAGE_TO_DECRYPT> ')
print('The original message is:')
decrypted_msg = ''
for decrypt_shift in range(0,25):
    for i in decrypt_message:
        if i.isalpha() and i.isupper():
            if ord(i) + decrypt_shift < 91:
                temp_letter = ord(i)
                temp_letter += decrypt_shift
                decrypted_msg += chr(temp_letter)
            else:
                temp_letter = ord(i)
                temp_letter += decrypt_shift
                temp_letter -= 91
                temp_letter += 65
                decrypted_msg += chr(temp_letter)
        elif i.isalpha() and i.islower():
            if ord(i) + decrypt_shift < 123:
                temp_letter = ord(i)
                temp_letter += decrypt_shift
                decrypted_msg += chr(temp_letter)
            else:
                temp_letter = ord(i)
                temp_letter += decrypt_shift
                temp_letter -= 123
                temp_letter += 97
                decrypted_msg += chr(temp_letter)
        else:
            decrypted_msg += i
    if decrypt_guess(decrypted_msg, dic_list) == 1:
        break
    else:
        decrypted_msg = ''
        continue
print(f'OUTPUT {decrypted_msg}')
print('The original message was encrypted with a shift of:')
if decrypt_shift == 0:
    print(f'OUTPUT {decrypt_shift}')
else:
    print(f'OUTPUT {26- decrypt_shift}')
