#Write a function that has a single string as its parameter, and returns the number of
#uppercase letters, and the number of lowercase letters in the string. Test the
#function with a short program.

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Test the function
input_string = input("Enter a string to test: ")
upper, lower = count_upper_lower(input_string)

print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")

