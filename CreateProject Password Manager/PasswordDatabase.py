"""
This program allows for the storage of a secure password database right on the users computer that can both create,
store, and access passwords.  This database functions off of a 256hash encrypted password that only the user knows and
is given to them at the time of download or purchase in theory and is required to access each time.
To further abstract the database from hackers the passwords and sites they are used for are encrypted with base 64
encoding and can be stored in any file and file extension the user would like.  This allows the user to abstract the
storage even further by placing it in an unknown directory an attacker might be looking for and with a file extension
that isn't just plain text.  This project incorporates encryption, cyber security, and steganography.  This is primarily
meant for Linux users as they will have the hardest time storing their passwords for websites securely compared to
Windows or Mac.  Thank you and please enjoy my project.
"""
# These are the libraries used within this program and are required to run it.
import hashlib
import random

# This is the user-specific hash key that is user and program specific
hashed_verify_key = b"H\xb9\x95x=\x9d\xe5l8\x1e\xfb\xc2\x9d\x1d\x9c\xa9U\xe3NvL\x1c\x9e\xe7;\x15N\xea\x98\x9f\xdcI"

# Welcome message and global variables
print('######                       #     #                      ', '#     #                                           ')
print('#     #   ##    ####   ####  #  #  #  ####  #####  #####  ', '##   ##   ##   #    #   ##    ####  ###### #####  ')
print('#     #  #  #  #      #      #  #  # #    # #    # #    # ', '# # # #  #  #  ##   #  #  #  #    # #      #    # ')
print('######  #    #  ####   ####  #  #  # #    # #    # #    # ', '#  #  # #    # # #  # #    # #      #####  #    # ')
print('#       ######      #      # #  #  # #    # #####  #    # ', '#     # ###### #  # # ###### #  ### #      #####  ')
print('#       #    # #    # #    # #  #  # #    # #   #  #    # ', '#     # #    # #   ## #    # #    # #      #   #  ')
print('#       #    #  ####   ####   ## ##   ####  #    # #####  ', '#     # #    # #    # #    #  ####  ###### #    # ')

print('Please enter your user verification key given to you at the installation of the program.')
verify_key = input('Enter Here: ')
verify_key = bytes(verify_key, 'utf-8')
random_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_'
password_list = []


# Function to verify the hash key
# Used a function because it helped abstract the idea of checking from my program
def verify_key_hash(verify_key):
    check_hash = hashlib.sha256(verify_key)
    if check_hash.digest() == hashed_verify_key:
        print('Success')
    else:
        print('Fail')
        quit()


# Function to create a random 16-character password for the user
def random_password(user_seed):
    s = 0
    random_user_password = ''
    random.seed(user_seed)
    while s < 16:
        random_user_password += random.choice(random_str)
        s += 1
    random_user_password = str(random_user_password)
    password_list.append(random_user_password)

# Function to write the created passwords to a list as well as the website they belong to
def pass_file_write(password_list):
    pass_file.write(password_list[0])
    pass_file.write(password_list[1])
    pass_file.write('\n')


# Function to search the file for the site and return the password
def pass_file_search(user_site):
    for i in pass_list:
        temp_pass = i
        temp_pass = temp_pass.split(' ')
        temp_decode = temp_pass[0]
        if temp_decode == user_site:
            temp_password = temp_pass[1]
            print(f'your password for the site {user_site} is {temp_password}')
        else:
            print(f'Your password was not found for the specified site.')
            print(f'Please try again.
            continue


# Runs the verify key function and if it fails it will always quit the program
# This helps protect against brute force attacks and ensures the password loop is never entered without the key
verify_key_hash(verify_key)

# Asks the user for a file they want to store the passwords in
print('Enter the file your passwords are stored in (This can have any file extension)')
user_file = input('File: ')
while True:
    # Gives the user 3 options for going through the program
    print('What would you like to do?')
    print('1. Exit')
    print('2. Create a Password')
    print('3. Access a Password')
    user_choice = int(input('Enter Here: '))

    # Quits the program when user wants to exit
    if user_choice == 1:
        quit()
    # Allows the user to add a site and password to the database
    elif user_choice == 2:
        with open(user_file, 'a') as pass_file:
            print('What site would you like to create a password for?')
            user_site = str(input('Site: '))
            user_site += ' '
            user_site = str(user_site)
            print('Would you like an auto-generated password or a user-created one?')
            print('1. auto-generated password')
            print('2. user-created')
            user_choice_generate = int(input('Enter Here: '))

            # Generates a 16-character random password- can actually change this length in the code if you'd like
            if user_choice_generate == 1:
                password_list = []
                print('Enter the seed with which you would like to generate a random 16-character password')
                user_seed = input('Seed: ')
                password_list.append(user_site)
                random_password(user_seed)

            # Allows the user to specify the password
            elif user_choice_generate == 2:
                password_list = []
                print('Enter the password that you would like to store to the specified site')
                user_password = input('Password: ')
                password_list.append(user_site)
                password_list.append(user_password)

            else:
                quit()
            pass_file_write(password_list)
    # Searches the database for the site the user would like and returns the matching ones
    elif user_choice == 3:
        with open(user_file, 'r') as pass_file:
            print('What site would you like to access?')
            user_site = input('Site: ')
            pass_list = pass_file.readlines()
            pass_file_search(user_site)
    else:
        quit()
