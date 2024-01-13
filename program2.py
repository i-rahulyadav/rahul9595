#Write a program that simulates the way in which a user might choose a password.
#The program should prompt for a new password, and then prompt again. If the two
#passwords entered are the same the program should say "Password Set" or
#similar, otherwise it should report an error.

def set_password():
    # Prompt the user to enter a new password
    password1 = input("Enter a new password: ")

    # Prompt the user to confirm the password
    password2 = input("Confirm your password: ")

    # Check if the passwords match
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")

# Call the set_password function
set_password()

