#Write a function that accepts a positive integer as a parameter and then returns a
#representation of that number in binary (base 2).
#Hint: This is in many ways a trick question. Think!


def decimal_to_binary(n):
    if n == 0:
        return '0b0'  # Binary representation of 0

    binary_representation = ''
    while n > 0:
        remainder = n % 2
        binary_representation = str(remainder) + binary_representation
        n //= 2

    return '0b' + binary_representation

# Example usage:
decimal_number = 42
binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")
