#Functions are often used to validate input. Write a function that accepts a single
#integer as a parameter and returns True if the integer is in the range 0 to 100
#(inclusive), or False otherwise. Write a short program to test the function.

def is_in_range(number):
    return 0 <= number <= 100

# Test the function
test_number = int(input("Enter an integer to test: "))
result = is_in_range(test_number)

if result:
    print(f"{test_number} is in the range 0 to 100.")
else:
    print(f"{test_number} is NOT in the range 0 to 100.")
