#Write a program that takes a URL as a command-line argument and reports
#whether or not there is a working website at that address.
#Hint: You need to get the HTTP response code.
#Another Hint: StackOverflow is your friend.

import sys
import requests

def check_website(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} returned a non-OK status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    check_website(url)
