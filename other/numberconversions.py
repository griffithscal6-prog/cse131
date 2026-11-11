

def get_number():
    """Obtain a positive integer from the user.
    Handle incorrect input: i.e., user enters negative number, floating point number, or text."""
    number = -1
    while number < 0:
        try:
            number = int(input("Please enter a positive integer: "))
            if number < 0:
                print("The number must be non-negative. Please try again.")
            return number
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
    return number
def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return "0"
    else:
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
        return binary
    
#def binary_to_decimal(b):
#    if not isinstance(b, str):
#        raise ValueError("Input must be a binary string.")
#    try:
#        return int(b, 2)
#    except ValueError:
#        raise ValueError("Invalid binary string.")
def decimal_to_hexadecimal(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return "0"
    else:
        hexadecimal = ""
        hex_chars = "0123456789ABCDEF"
        while n > 0:
            hexadecimal = hex_chars[n % 16] + hexadecimal
            n //= 16
        return hexadecimal
#def hexadecimal_to_decimal(h):
#    if not isinstance(h, str):
#        raise ValueError("Input must be a hexadecimal string.")
#    try:
#        return int(h, 16)
#    except ValueError:
#        raise ValueError("Invalid hexadecimal string.")
def decimal_to_octal(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return "0"
    else:
        octal = ""
        while n > 0:
            octal = str(n % 8) + octal
            n //= 8
        return octal
#def octal_to_decimal(o):
#    if not isinstance(o, str):
#        raise ValueError("Input must be an octal string.")
#    try:
#        return int(o, 8)
#    except ValueError:
#        raise ValueError("Invalid octal string.")
def main():
    # Test the conversion functions
    decimal_number = get_number()

    binary_number = decimal_to_binary(decimal_number)
    print(f"Decimal {decimal_number} to Binary: {binary_number}")

    #decimal_from_binary = binary_to_decimal(binary_number)
    #print(f"Binary {binary_number} to Decimal: {decimal_from_binary}")

    hexadecimal_number = decimal_to_hexadecimal(decimal_number)
    print(f"Decimal {decimal_number} to Hexadecimal: {hexadecimal_number}")

    #decimal_from_hexadecimal = hexadecimal_to_decimal(hexadecimal_number)
    #print(f"Hexadecimal {hexadecimal_number} to Decimal: {decimal_from_hexadecimal}")

    octal_number = decimal_to_octal(decimal_number)
    print(f"Decimal {decimal_number} to Octal: {octal_number}")

    #decimal_from_octal = octal_to_decimal(octal_number)
    #print(f"Octal {octal_number} to Decimal: {decimal_from_octal}")

main()