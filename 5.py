#Another way to hide a message is to include the letters that make it up within
#seemingly random text. The letters of the message might be every fifth character,
#for example. Write and test a function that does such encryption. It should
#randomly generate an interval (between 2 and 20), space the message out
#accordingly, and should fill the gaps with random letters. The function should
#return the encrypted message and the interval used.
#For example, if the message is "send cheese", the random interval is 2, and for
#clarity the random letters are not random:
#send cheese
#s e n d c h e e s e
#sxyexynxydxy cxyhxyexyexysxye

import random
import string

def random_encrypt(message):
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Create a list to hold the encrypted characters
    encrypted_chars = []
    
    # Iterate through the message
    for i, char in enumerate(message):
        # Include the letter of the message every 'interval' characters
        if char.isalpha():
            if i % interval == 0:
                encrypted_chars.append(char)
            else:
                # Fill the gaps with random letters
                random_letter = random.choice(string.ascii_lowercase)
                encrypted_chars.append(random_letter)
    
    # Construct the encrypted message
    encrypted_message = ''.join(encrypted_chars)
    
    return encrypted_message, interval

# Test the function
original_message = "send cheese"
encrypted_message, interval_used = random_encrypt(original_message)

print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {interval_used}")
