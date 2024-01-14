#Write and test a function that determines if a given integer is a prime number. A
#prime number is an integer greater than 1 that cannot be produced by multiplying
#two other integers.

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check for factors up to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Test the function
test_numbers = [2, 7, 15, 19, 25, 29, 31]

for number in test_numbers:
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
