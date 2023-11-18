## Challenge Name: Web technologies: extract elements from a web page
**Category:** Web

**Challenge Description:**

In this challenge the letters highlighted on the web page accessible at the URL http://web-13.challs.olicyber.it/ form the flag. The goal is to isolate them from the rest of the page and concatenate them. 

N.B.: in this challenge the flag is presented without its typical ```flag{``` frame. This is normal when it is found in contexts where it would be difficult to insert it (for example due to the curly bracket), but it is still necessary to add it manually before sending the flag for it to be recognized.
### Approach

As descripted in the challenge description to solve this challenge is necessary to get the flag from the highlighted words inside the website.

The solution to this challenge is this [script](/olicyber-training/web/13-Extract-elements/solve.py):

```
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

```

**Flag**

```
flag{donotrecommenddoingthisbyhand}
```
### Reflections
Easy difficulty starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
