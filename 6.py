#Write a program that decrypts messages encoded as above.

def random_decrypt(encrypted_message, interval_used):
    # Create a list to hold the decrypted characters
    decrypted_chars = []

    # Iterate through the encrypted message
    for i, char in enumerate(encrypted_message):
        # Include the letter of the message every 'interval_used' characters
        if char.isalpha():
            if i % interval_used == 0:
                decrypted_chars.append(char)

    # Construct the decrypted message
    decrypted_message = ''.join(decrypted_chars)

    return decrypted_message

# Example usage:
encrypted_message = "sxyexynxydxy cxyhxyexyexysxye"
interval_used = 2

decrypted_message = random_decrypt(encrypted_message, interval_used)

print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
