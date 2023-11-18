import requests
from bs4 import BeautifulSoup

# URL of the target website
url = 'http://web-13.challs.olicyber.it/'

# Send a GET request to the website
response = requests.get(url)
html_text = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_text, 'html.parser')

# Initialize an empty string to store the flag
flag = ''

# Search through the HTML for elements with the class 'red'
for highlighted_ch in soup.find_all(attrs="red"):
    # Concatenate each highlighted character to build the flag
    flag += highlighted_ch.string

# Enclose the collected characters in the 'flag{}' format
flag = 'flag{' + flag + '}'

# Print the final flag
print(flag)
