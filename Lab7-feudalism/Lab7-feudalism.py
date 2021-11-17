#   Garrett Thompson
#   CSCI 101 – Section H
#   Python Lab 7
#   References: Went to ALS, me and my friend Will worked together on pseudocode and the math for the classes
#   Time: 2.5 hours
#   (1 hour of which was comprised of me trying to change a string in a list into an integer without using another list)
#   (Also accidentally created a 3-D array at one point)

"""
This code takes in a name and up to 5 classes for a person and then sorts them based on both class and number
It works by assigning a value to each class based on if it's upper, middle, and lower, and where it is in the list
It consists primarily of loops that manipulate the strings in the list and eventually output a 2D array
That 2D array is then sorted through python's built-in sort function and a lambda key
Finally I output the sorted names
"""

# Takes in number of people that will be sorted
print('Input the number of people to sort:')
num_people = int(input('NUM_PEOPLE> '))

# This initializes all of the variables: any variable with a single letter is just an iterator and is not important
i = 0
# Keeps track of the final class sum
class_sum = 0
# Temporary list inside of the main loop to mutate strings and lists
temp_list = []
# A list comprised of the name of the person that is currently being mutated
name_list = []
# A list comprised of the classes that is currently being mutated
class_list = []
# A list used at the end to append both name and class sum to
almost_final_list = []
# A list used to store the final 2-D array and what is sorted
final_list = []

# The main "for" loop based on the number of people that are being sorted
for n in range(num_people):

    # Resetting all important non permanent variables before each loop- see above for variable explanation
    i = 0
    class_sum = 0
    temp_list = []
    name_list = []
    class_list = []
    almost_final_list = []

    # This variable takes in the name and classes of the person currently being mutated
    temp_person = input(f'PERSON{n}> ')

    # Replaces class in the list because it looked nice when debugging
    # You will never see this, but I wanted to do it :)
    temp_list = temp_person.replace(' class', '')

    # Splits list based on the colon given in the input which allows us to call the name later on
    name_list = temp_list.split(': ', 1)
    # Splits list again based on just the class part and hyphens and comprises of the main list we will be changing
    class_list = name_list[1].split('-')

    # A while loop to change each class to an integer in string form that we can later typecast into an actual integer
    # Not sure how to directly change to an integer without creating a whole different list, I think python is just dumb
    # Please let me know if there is a way, it would be super useful
    while i < len(class_list):
        # Conditionals to determine what to change each class too, in reverse because if not it will cause the list to
        # sort backwards alphabetically
        if 'middle' == class_list[i]:
            del class_list[i]
            class_list.insert(i, '2')
        elif 'upper' == class_list[i]:
            del class_list[i]
            class_list.insert(i, '1')
        else:
            del class_list[i]
            class_list.insert(i, '3')
        i += 1
    i = 0

    # Another conditional to determine if our class list contains the max classes because if not it will not be able to
    # sort properly
    if len(class_list) < 5:
        while i < 5 - len(class_list):
            class_list.insert(i, '2')
    i = 0

    # Apply base 10 math here to each index of the class list because it gives values big enough to allow for no
    # accidents in sorting
    while i < len(class_list):
        class_sum += (int(class_list[i]) * (10 ** i))
        i += 1

    # This appends the temporary almost final list each loop so that I can add it into a 2-D array
    almost_final_list.append(name_list[0])
    almost_final_list.append(class_sum)

    # This creates a 2-D array for me and allows me to sort it eventually after the loop is complete
    final_list.append(almost_final_list)

# This sort function performs some sort of magic on the list and magically knows to sort by number then alphabet
# I would love an in depth explanation of the lambda function because from what I can gather from the internet
# it should be a function we define, but obviously I'm not defining it
sorted_by_class_then_name = sorted(final_list, key=lambda person: (person[1], person[0]))

# Final loop to iterate over the sorted 2-D array and only print out the name according to proper output formatting
print('After sorting, the list from highest to lowest is as follows:')
for j in sorted_by_class_then_name:
    print(f'OUTPUT {j[0]}')
