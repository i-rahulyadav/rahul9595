#Modify the previous program so that it can process any number of values. The input
#terminates when the user just pressed "Enter" at the prompt rather than entering a
#value

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Input validation and temperature conversion function
def process_temperature_input(input_str):
    if not input_str:
        return None  # Return None for an empty input

    try:
        temperature = float(input_str[:-1])
        if input_str[-1].upper() == 'C':
            return temperature
        else:
            raise ValueError("Invalid input format. Temperature must be followed by 'C'.")
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Read temperatures until the user just presses "Enter"
temperatures = []

while True:
    user_input = input("Enter a temperature in Celsius (or press Enter to finish): ")
    celsius_temperature = process_temperature_input(user_input)

    if celsius_temperature is not None:
        temperatures.append(celsius_temperature)
    else:
        break  # Exit the loop if the user just pressed "Enter"

# Display maximum, minimum, and mean temperatures
if temperatures:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print("\nTemperature Statistics:")
    print(f"Maximum temperature: {max_temp:.2f}C / {celsius_to_fahrenheit(max_temp):.2f}F")
    print(f"Minimum temperature: {min_temp:.2f}C / {celsius_to_fahrenheit(min_temp):.2f}F")
    print(f"Mean temperature: {mean_temp:.2f}C / {celsius_to_fahrenheit(mean_temp):.2f}F")
else:
    print("No valid temperatures entered.")
