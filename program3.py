#Modify your previous program so that the password must be between 8 and 12
#characters (inclusive) long

def set_password():
    # Prompt the user to enter a new password
    password1 = input("Enter a new password (8-12 characters): ")

    # Check the length of the password
    if 8 <= len(password1) <= 12:
        # Prompt the user to confirm the password
        password2 = input("Confirm your password: ")

        # Check if the passwords match
        if password1 == password2:
            print("Password Set")
        else:
            print("Error: Passwords do not match. Please try again.")
    else:
        print("Error: Password must be between 8 and 12 characters long.")

# Call the set_password function
set_password()
