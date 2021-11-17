#  Garrett Thompson
#  CSCI 102 – Section A
#  Extra Credit Lab - Hangman
#  References:
#  Time: 45 minutes
print('Welcome to Simple Hang Man')
print('Enter a secret word:')
secret_word = input('WORD> ')
print('Enter the number of guesses allowed:')
num_guesses = int(input('NUM> '))
i = 0
guess_list = []
correct_guess_str = ''


while i < num_guesses:
    print('Please enter a character:')
    current_char = input('CHAR> ')
    i += 1
    if (current_char not in secret_word or current_char in guess_list) and i == num_guesses:
        print(f'OUTPUT You ran out of guesses! Better luck next time!')
        correct_guess_str = ''
        for n in secret_word:
            guess_list.append(n)
        for n in secret_word:
            u = 0
            while u < len(guess_list):
                if guess_list[u] == n:
                    correct_guess_str += n
                    correct_guess_str += ' '
                    break
                elif guess_list[u] != n and u == len(guess_list) - 1:
                    correct_guess_str += '_'
                    correct_guess_str += ' '
                    break
                u += 1
        print(f'OUTPUT Secret word: {correct_guess_str}\n')
        break
    else:
        if current_char in guess_list:
            print('OUTPUT Boo! You guessed incorrectly')
            print(f'{num_guesses - i} guesses remaining')
            print(f"Character's guessed: {guess_list}")
            correct_guess_str = ''
            for n in secret_word:
                u = 0
                while u < len(guess_list):
                    if guess_list[u] == n:
                        correct_guess_str += n
                        correct_guess_str += ' '
                        break
                    elif guess_list[u] != n and u == len(guess_list) - 1:
                        correct_guess_str += '_'
                        correct_guess_str += ' '
                        break
                    u += 1
            print(f'OUTPUT Secret word: {correct_guess_str}\n')
        elif current_char not in guess_list:
            guess_list.append(current_char)
            correct_guess_str = ''
            for n in secret_word:
                u = 0
                while u < len(guess_list):
                    if guess_list[u] == n:
                        correct_guess_str += n
                        correct_guess_str += ' '
                        break
                    elif guess_list[u] != n and u == len(guess_list) - 1:
                        correct_guess_str += '_'
                        correct_guess_str += ' '
                        break
                    u += 1
            if '_' not in correct_guess_str:
                print('OUTPUT Congratulations! You guessed the secret word!')
                print(f'{num_guesses - i} guesses remaining')
                print(f'OUTPUT Secret word: {correct_guess_str}\n')
                break
            elif current_char in secret_word:
                print(f'OUTPUT Success! You guessed a character in the word!')
                print(f'{num_guesses - i} guesses remaining')
                print(f"Character's guessed: {guess_list}")
                print(f'OUTPUT Secret word: {correct_guess_str}\n')
                continue
            elif current_char not in secret_word:
                print(f'OUTPUT Boo! You guessed incorrectly')
                print(f'{num_guesses - i} guesses remaining')
                print(f"Character's guessed: {guess_list}")
                print(f'OUTPUT Secret word: {correct_guess_str}\n')
                continue
