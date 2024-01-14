#Write a program that takes the name of a file as a command-line argument, and
#creates a backup copy of that file. The backup should contain an exact copy of the
#contents of the original and should, obviously, have a different name.
#Hint: By now, you should be getting the idea that there is a built-in way to do the
#heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.

import sys
import shutil

def create_backup(file_path):
    try:
        # Append ".bak" to the original file name to create a backup copy
        backup_path = file_path + ".bak"
        
        # Use shutil.copy2 to preserve metadata (timestamps, etc.)
        shutil.copy2(file_path, backup_path)
        
        print(f"Backup created successfully: {backup_path}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_backup.py <file_path>")
        sys.exit(1)

    file_to_backup = sys.argv[1]
    create_backup(file_to_backup)
