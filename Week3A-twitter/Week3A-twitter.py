#   Garrett Thompson
#   CSCI 102 – Section A
#   Week 3 - Lab A - Twitter Decoding
#   References: Took Zybook code and expanded on it upon request by assignment
#   Time: 20 minutes

print('Enter the Tweet or Message abbreviation to decode.')
tweet = input('TWEET>')

if tweet == 'LOL':
    print('The decoded abbreviation is:')
    print('OUTPUT LOL = Laughing Out Loud')

elif tweet == 'BFN':
    print('The decoded abbreviation is:')
    print('OUTPUT BFN = Bye For Now')

elif tweet == 'FTW':
    print('The decoded abbreviation is:')
    print('OUTPUT FTW = For The Win')

elif tweet == 'IRL':
    print('The decoded abbreviation is:')
    print('OUTPUT IRL = In Real Life')

elif tweet == 'BTW':
    print('The decoded abbreviation is:')
    print('OUTPUT BTW = By The Way')

elif tweet == 'DM':
    print('The decoded abbreviation is:')
    print('OUTPUT DM = Direct Message')

elif tweet == 'AFAIK':
    print('The decoded abbreviation is:')
    print('OUTPUT AFAIK = As Far As I Know')

elif tweet == 'IDK':
    print('The decoded abbreviation is:')
    print("OUTPUT IDK = I Don't Know")

else:
    print("OUTPUT Sorry, don't know that one")
