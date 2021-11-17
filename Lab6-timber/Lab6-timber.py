# Garrett Thompson
# CSCI 101 – Section B
# Python Lab 6: Timber Regrowth
# References:
# Time: 30 minutes
print('Input the number of years to print in the reforestation table:')
num_years = int(input('YEARS> '))
print('The reforestation table is then')
print('Year, # Acres, % of Forest')
num_acres = 3000
num_acres_available = 12000
num_acres_now = num_acres
for i in range(num_years + 1):
    print(f'OUTPUT {i}, {num_acres_now:.1f}, {(num_acres_now/num_acres_available * 100):.2f}%')
    num_acres_now = num_acres_now + .03 * num_acres_now

print(f'OUTPUT 47')
