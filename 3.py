#Write a program that takes a bunch of command-line arguments, and then prints
#out the shortest. If there is more than one of the shortest length, any will do.
#Hint: Don't overthink this. A good way to find the shortest is just to sort them

import sys

def find_shortest_argument(arguments):
    if not arguments:
        print("No command-line arguments provided.")
        return None

    shortest_argument = min(arguments, key=len)
    return shortest_argument

if __name__ == "__main__":
    # Exclude the program name (sys.argv[0])
    arguments = sys.argv[1:]

    shortest_arg = find_shortest_argument(arguments)

    if shortest_arg:
        print(f"The shortest command-line argument is: {shortest_arg}")
