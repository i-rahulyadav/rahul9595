#Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
#Hint: You should know there are built-in functions for max and min. If you hunt, you
#might also find one for the mean.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Input validation and temperature conversion function
def process_temperature_input(input_str):
    try:
        temperature = float(input_str[:-1])
        if input_str[-1].upper() == 'C':
            return temperature
        else:
            raise ValueError("Invalid input format. Temperature must be followed by 'C'.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Read 6 temperatures from the user
temperatures = []
for i in range(1, 7):
    user_input = input(f"Enter temperature {i} in Celsius (e.g., 25C): ")
    celsius_temperature = process_temperature_input(user_input)
    if celsius_temperature is not None:
        temperatures.append(celsius_temperature)

# Display maximum, minimum, and mean temperatures
if temperatures:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print(f"\nMaximum temperature: {max_temp:.2f}C / {celsius_to_fahrenheit(max_temp):.2f}F")
    print(f"Minimum temperature: {min_temp:.2f}C / {celsius_to_fahrenheit(min_temp):.2f}F")
    print(f"Mean temperature: {mean_temp:.2f}C / {celsius_to_fahrenheit(mean_temp):.2f}F")
else:
    print("No valid temperatures entered.")
