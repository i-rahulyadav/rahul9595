#Last week you wrote a program that processed a collection of temperature readings
#entered by the user and displayed the maximum, minimum, and mean. Create a
#version of that program that takes the values from the command-line instead. Be
#sure to handle the case where no arguments are provided!

import sys

def process_temperatures(temperatures):
    if not temperatures:
        print("No temperatures provided.")
        return

    try:
        temperatures = list(map(float, temperatures))
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)

        print(f"Maximum temperature: {max_temp}")
        print(f"Minimum temperature: {min_temp}")
        print(f"Mean temperature: {mean_temp}")
    except ValueError:
        print("Error: Please provide valid numerical temperature values.")

if __name__ == "__main__":
    # Exclude the program name (sys.argv[0])
    temperature_values = sys.argv[1:]

    process_temperatures(temperature_values)
