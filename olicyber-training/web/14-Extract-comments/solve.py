import requests
from bs4 import BeautifulSoup, Comment

# URL of the target website
url = 'http://web-14.challs.olicyber.it/'

# Send a GET request to the website
response = requests.get(url)
html_text = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_text, 'html.parser')

# Define a function to check if a tag is a comment
def is_comment(tag):
    return isinstance(tag, Comment)

# Find all comments in the HTML
comments = soup.find_all(string=is_comment)

# Extract the flag from comments
for comment in comments:
    if 'flag{' in comment:
        flag_content = comment.split('flag{')[1].split('}')[0]
        flag = f'flag{{{flag_content}}}'
        print(flag)
        break
