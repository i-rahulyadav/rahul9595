#Write a program that takes a centigrade temperature and displays the equivalent in
#fahrenheit. The input should be a number followed by a letter C. The output should
#be in the same format.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input format validation function
def validate_input(input_str):
    try:
        # Extract the numeric part from the input string
        temperature = float(input_str[:-1])
        
        # Check if the last character is 'C'
        if input_str[-1].upper() == 'C':
            return temperature
        else:
            raise ValueError("Invalid input format. Temperature must be followed by 'C'.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Get temperature input from the user
user_input = input("Enter temperature in Celsius (e.g., 25C): ")

# Validate input and convert temperature
celsius_temperature = validate_input(user_input)
if celsius_temperature is not None:
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    print(f"{user_input} is equal to {fahrenheit_temperature:.2f}F")
