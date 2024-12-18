__import__("os").system("pip install requests --target=. -qq")

import requests

# Define the URL
url = "https://api.github.com"

try:
    # Send a GET request
    response = requests.get(url)
    
    # Raise an exception for HTTP errors
    response.raise_for_status()
    
    # Print the response text
    print("Response:")
    print(response.text)
    
    # Optionally, print JSON response (if applicable)
    print("\nJSON Response:")
    print(response.json())

except requests.exceptions.RequestException as e:
    # Print the error if any
    print(f"An error occurred: {e}")
