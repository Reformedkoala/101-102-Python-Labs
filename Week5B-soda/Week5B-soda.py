#   John Henke
#   CSCI 102 – Section A
#   Week 5 - Lab B - Soda Sprinter
#   References:
#   Time: 30 minutes
print("Enter the number of empty bottles in Blaster's possession at the start of the day.")
empty_bottles_start = int(input('EMPTIES> '))
print('Enter the number of empty bottles that Blaster found during the day.')
empty_found = int(input('FOUND> '))
print('Enter the number of empty soda bottles required to buy a new soda.')
amount_cost = int(input('COST> '))
empty_bottles_total = empty_found + empty_bottles_start
bottles_drunk = 0

while empty_bottles_total >= amount_cost:
    empty_bottles_remainder = empty_bottles_total % amount_cost
    empty_bottles_total = empty_bottles_total // amount_cost
    bottles_drunk += empty_bottles_total + empty_bottles_remainder

print('The total number of sodas that Blaster drank is:')
print(f'OUTPUT {bottles_drunk}')
