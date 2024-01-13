#Modify your program a final time so that it executes until the user successfully
#chooses a password. That is, if the password chosen fails any of the checks, the
#program should return to asking for the password the first time.

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

def set_password():
    while True:
        # Prompt the user to enter a new password
        password1 = input("Enter a new password (8-12 characters): ")

        # Check the length of the password
        if 8 <= len(password1) <= 12:
            # Check if the password is not in the list of common passwords
            if password1 not in BAD_PASSWORDS:
                # Prompt the user to confirm the password
                password2 = input("Confirm your password: ")

                # Check if the passwords match
                if password1 == password2:
                    print("Password Set")
                    break  # Exit the loop if the password is set successfully
                else:
                    print("Error: Passwords do not match. Please try again.")
            else:
                print("Error: Common passwords are not allowed. Please choose a different password.")
        else:
            print("Error: Password must be between 8 and 12 characters long.")

# Call the set_password function
set_password()

