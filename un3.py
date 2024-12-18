import requests
import random
import string
import concurrent.futures
import os
from colorama import Fore, Style

url = "https://www.instagram.com/api/v1/users/check_username/"

headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    'x-csrftoken': "lu1I3sjgfNCvYGYFEtW99n",
    'Content-Type': "application/x-www-form-urlencoded"
}

# Ensure the output directory exists
output_dir = "insta_usernames"
os.makedirs(output_dir, exist_ok=True)

def random_username():
    # Generate a 4-5 character username with a dot in a valid position
    length = 3
    base = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    dot_position = random.randint(1, length - 2) if length > 3 else 2
    return base
    return base[:dot_position] + '' + base[dot_position:]

def check_username():
    username = "_." + random_username()
    payload = {"username": username}  # Use a dictionary to pass form data
    try:
        response = requests.post(url, data=payload, headers=headers)

        # Check for status code 429 (rate limit exceeded)
        if response.status_code == 429:
            print("You got blocked. Change your IP.")
            # Shutdown the executor to stop further requests
            executor.shutdown(wait=False)
            return

        response_data = response.json()
        
        # Extract availability if present
        availability = response_data.get("available")
        
        # Check if `availability` is None, meaning the property is missing
        if availability is None:
            print("Service temporarily unavailable. Please try again later.")
            # Shutdown the executor to stop further requests
            executor.shutdown(wait=False)
            return
        
        # Color the output and append to file if available
        color = Fore.GREEN if availability else Fore.RED
        print(f"{color}Username: {username} - Available: {availability}, Status Code: {response.status_code}{Style.RESET_ALL}")
        
        if availability:
            # Append to the specified file in the output directory
            with open(os.path.join(output_dir, "3.txt"), "a") as file:
                file.write(f"{username}\n")

    except requests.RequestException as e:
        print(f"Request failed for username {username}: {e}")

# Execute requests concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(check_username) for _ in range(3000)]
    concurrent.futures.wait(futures)
