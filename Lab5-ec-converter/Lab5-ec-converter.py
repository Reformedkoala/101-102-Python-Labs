#  Garrett Thompson
#  CSCI 101 – Section H
#  Python Lab 5
#  References:
#  Time: 180 minutes
continue_var = ''
print('Welcome to the Binary-Hex-Decimal Converter')
print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
while 0 == 0:
    print('Enter an option:')
    print('1. Binary-Decimal Conversion')
    print('2. Decimal-Binary Conversion')
    print('3. Hexadecimal-Decimal Conversion')
    print('4. Decimal-Hexadecimal Conversion')
    print('5. Quit')
    option = input('OPTION> ')
    i = 0
    for k in option:
        if option[i] == '1' or option[i] == '2' or option[i] == '3' or option[i] == '4' or option[i] == '5':
            i += 1
        else:
            print('ERROR: Please choose from [1-5]')
            print('OUTPUT ERROR')
            break
    if option == '1':
        i = 0
        binary_str = input('BINARY-STR> ')
        for u in binary_str:
            if binary_str[i] == '0' or binary_str[i] == '1':
                i += 1
                continue
            else:
                print(f'ERROR: Input {binary_str} is NOT a binary number.')
                print('OUTPUT ERROR')
                i = 0
                break
        if i != 0:
            decimal_final = 0
            i = -1
            p = 0
            for n in binary_str:
                decimal_final += int(binary_str[i]) * (2 ** p)
                i -= 1
                p += 1
            print(f'Binary {binary_str} is Decimal {decimal_final}')
            print(f'OUTPUT {decimal_final}')
        else:
            i = 0
    elif option == '2':
        decimal_in = input('DECIMAL-STR> ')
        i = 0
        for v in decimal_in:
            if decimal_in[i] == '0' or decimal_in[i] == '1' or decimal_in[i] == '2' or decimal_in[i] == '3'\
                    or decimal_in[i] == '4' or decimal_in[i] == '5' or decimal_in[i] == '6' or decimal_in[i] == '7'\
                    or decimal_in[i] == '8' or decimal_in[i] == '9':
                i += 1
                continue
            else:
                print(f'ERROR: Input {decimal_in} is NOT a decimal number.')
                print('OUTPUT ERROR')
                i = 0
                break
        if i != 0:
            int(decimal_in)
            binary_final = ''
            binary_str = ''
            decimal_number = int(decimal_in)
            remainder = 0
            if int(decimal_in) == 0:
                print(f'Decimal {decimal_in} is Binary 0')
                print(f'OUTPUT 0')
            else:
                while decimal_number > 0:
                    remainder = decimal_number % 2
                    decimal_number = decimal_number // 2
                    binary_final += str(remainder)
                for n in reversed(binary_final):
                    binary_str += str(n)
                print(f'Decimal {decimal_in} is Binary {binary_str}')
                print(f'OUTPUT {binary_str}')
        else:
            i = 0
    elif option == '3':
        hex_str = str(input('HEX-STR> '))
        i = 0
        for k in hex_str:
            if hex_str[i] == '0' or hex_str[i] == '1' or hex_str[i] == '2' or hex_str[i] == '3' or hex_str[i] == '4' \
                    or hex_str[i] == '5' or hex_str[i] == '6' or hex_str[i] == '7' or hex_str[i] == '8' \
                    or hex_str[i] == '9' or hex_str[i] == 'A' or hex_str[i] == 'B' or hex_str[i] == 'C' \
                    or hex_str[i] == 'D' or hex_str[i] == 'E' or hex_str[i] == 'F':
                i += 1
                continue
            else:
                print(f'ERROR: Input {hex_str} is NOT a hexadecimal number.')
                print('OUTPUT ERROR')
                i = 0
                break
        hexadecimal_final = 0
        j = -1
        q = 0
        if i != 0:
            for k in hex_str:
                if hex_str[j] == "A" or hex_str[j] == "B" or hex_str[j] == "C" or hex_str[j] == "D"\
                        or hex_str[j] == "E" or hex_str[j] == "F":
                    hexadecimal_final += int(ord(hex_str[j]) - 55) * (16 ** q)
                    j -= 1
                    q += 1
                else:
                    hexadecimal_final += int(hex_str[j]) * (16 ** q)
                    j -= 1
                    q += 1
            print(f'Hexadecimal {hex_str} is Decimal {hexadecimal_final}')
            print(f'OUTPUT {hexadecimal_final}')
        else:
            i = 0
    elif option == '4':
        decimal_in = input('DECIMAL-STR> ')
        i = 0
        for c in decimal_in:
            if decimal_in[i] == '0' or decimal_in[i] == '1' or decimal_in[i] == '2' or decimal_in[i] == '3' or \
                    decimal_in[i] == '4' or decimal_in[i] == '5' or decimal_in[i] == '6' or decimal_in[i] == '7' or \
                    decimal_in[i] == '8' or decimal_in[i] == '9':
                i += 1
                continue
            else:
                print(f'ERROR: Input {decimal_in} is NOT a decimal number.')
                print('OUTPUT ERROR')
                i = 0
                break
        if i != 0:
            int(decimal_in)
            hexadecimal_final = ''
            hexadecimal_str = ''
            hexadecimal_number = int(decimal_in)
            remainder = 0
            if int(decimal_in) == 0:
                print(f'Decimal {decimal_in} is Hexadecimal 0')
                print(f'OUTPUT 0')
            else:
                while hexadecimal_number > 0:
                    remainder = hexadecimal_number % 16
                    if remainder > 9:
                        remainder += 55
                        hexadecimal_final += str(chr(remainder))
                    else:
                        hexadecimal_final += str(remainder)
                    hexadecimal_number = hexadecimal_number // 16
                for r in reversed(hexadecimal_final):
                    hexadecimal_str += str(r)
                print(f'Decimal {decimal_in} is Hexadecimal {hexadecimal_str}')
                print(f'OUTPUT {hexadecimal_str}')
        else:
            i = 0
    elif option == '5':
        print('OUTPUT Goodbye!')
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break

    print('Would you like to continue (y/n)?')
    continue_var = input('CONTINUE> ').lower()
    if ('n' or 'no') in continue_var:
        print('OUTPUT Goodbye!')
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        break
    elif ('y' or 'yes') in continue_var:
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        continue
    else:
        print('OUTPUT ERROR')
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
# TO DO Fix Binary and Hexadecimal output of 0
