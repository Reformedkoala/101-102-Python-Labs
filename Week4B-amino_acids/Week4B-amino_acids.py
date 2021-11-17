#   Garrett Thompson
#   CSCI 101 – Section A
#   Week 4 - Lab B - Amino Acids
#   References:
#   Time: 20 Minutes
print('Input the chemical elements of the amino acid:')
carbon = input('CARBON> ')
hydrogen = input('HYDROGEN> ')
nitrogen = input('NITROGEN> ')
oxygen = input('OXYGEN> ')
sulfur = input('SULFUR> ')

if carbon == '3' and hydrogen == '7' and nitrogen == '1' and oxygen == '2':
    if sulfur == '0':
        print('The amino acid for 3C--7H--1N--2O--0S is Alanine')
        print('OUTPUT 3C--7H--1N--2O--0S')
        print('OUTPUT Alanine')
    else:
        print('The amino acid for 3C--7H--1N--2O--1S is Cysteine')
        print('OUTPUT 3C--7H--1N--2O--1S')
        print('OUTPUT Cysteine')
elif carbon == '6':
    if hydrogen == '14' and nitrogen == '4' and oxygen == '2':
        print('The amino acid for 6C--14H--4N--2O--0S is Arginine')
        print('OUTPUT 6C--14H--4N--2O--0S')
        print('OUTPUT Arginine')
    else:
        print('The amino acid for 6C--9H--3N--2O--0S is Histidine')
        print('OUTPUT 6C--9H--3N--2O--0S')
        print('OUTPUT Histidine')
elif carbon == '4':
    print('The amino acid for 4C--8H--2N--3O--0S is Asparagine')
    print('OUTPUT 4C--8H--2N--3O--0S')
    print('OUTPUT Asparagine')
elif carbon == '5':
    print('The amino acid for 5C--10H--2N--3O--0S is Glutamine')
    print('OUTPUT 5C--10H--2N--3O--0S')
    print('OUTPUT Glutamine')
else:
    print('Not and Amino Acid')
