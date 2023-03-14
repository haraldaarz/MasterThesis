import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json

# Set the path to the folder where screenshots will be saved
screenshot_folder = "screenshots"

# Create the folder if it does not exist
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Set the path to the file containing the IP addresses
ip_file = "ips.txt"

# Set the path to the file where the website information will be stored
info_file = "website_info.json"

# Initialize a list to store website information
website_info = []

# Read the IP addresses from the file
with open(ip_file) as ip_f:
    ips = ip_f.read().splitlines()

    # Loop through the IP addresses
    for ip in ips:
        try:
            # Check if the IP address is hosting a web server
            response = requests.get("http://" + ip, timeout=4)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string
            
            # Capture a screenshot of the homepage
            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            driver = webdriver.Chrome(options=options)
            driver.get("http://" + ip)
            screenshot_path = os.path.join(screenshot_folder, f"{ip}.png")
            driver.save_screenshot(screenshot_path)
            driver.quit()

            # Print a message indicating that the screenshot was captured
            print(f"Screenshot captured for {ip} ({title})")

            # Add the IP address and website information to the list
            website_info.append({
                "ip": ip,
                "title": title,
                "screenshot": screenshot_path
            })
        except requests.exceptions.Timeout:
            # If the IP address did not respond within 4 seconds, move on to the next IP
            print(f"Request timed out for {ip}")
            continue
        except:
            # If there is any other error, move on to the next IP
            print(f"Error occurred while processing {ip}")
            continue

# Write the website information to the file as JSON data
with open(info_file, "w") as f:
    json.dump(website_info, f)
