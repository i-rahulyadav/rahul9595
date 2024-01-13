#Modify your "greetings" program so that the first letter of the name entered is
#always in uppercase with the rest in lowercase. This should happen even if the user
#entered their name differently. So if the user entered arthur, ARTHUR, or even
#arTHur the name should be displayed as Arthur.

def greet_user():
    user_name = input("Enter your name: ")
    formatted_name = user_name.capitalize()  # Capitalize the first letter, make the rest lowercase

    print(f"Hello, {formatted_name}!")

# Test the function
greet_user()
