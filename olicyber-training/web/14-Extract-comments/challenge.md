## Challenge Name: Web technologies: extract comments from a web page
**Category:** Web

**Challenge Description:**

HTML documents can contain comments. These are completely ignored by the browser and do not participate in the construction of the content of the page but sometimes, due to the author's carelessness, they can contain interesting and potentially sensitive information.

The flag for this challenge is in a comment on the web page accessible via the address http://web-14.challs.olicyber.it/. The goal is to extract and display the comments contained on the page.
### Approach

As descripted in the challenge description to solve this challenge is necessary to get the flag from the web page comments.

The solution to this challenge is this [script](/olicyber-training/web/14-Extract-comments/solve.py):

```
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


```

**Flag**

```
flag{50m3b0dy_f0rg07_70_d31373_7hi5}
```
### Reflections
Easy difficulty starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
