#Write and test a function that converts a temperature measured in degrees
#centigrade into the equivalent in fahrenheit, and another that does the reverse
#conversion. Test both functions. (Google will find you the formulae).

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the functions
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_result = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input}°C is equal to {fahrenheit_result:.2f}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input}°F is equal to {celsius_result:.2f}°C")

