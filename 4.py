#Computers are commonly used in encryption. A very simple form of encryption
#(more accurately "obfuscation") would be to remove the spaces from a message
#and reverse the resulting string. Write, and test, a function that takes a string
#containing a message and "encrypts" it in this way.

def simple_encrypt(message):
    # Remove spaces
    message_without_spaces = message.replace(" ", "")
    
    # Reverse the string
    encrypted_message = message_without_spaces[::-1]
    
    return encrypted_message

# Test the function
original_message = "This is a simple encryption example."
encrypted_message = simple_encrypt(original_message)

print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted_message}")
