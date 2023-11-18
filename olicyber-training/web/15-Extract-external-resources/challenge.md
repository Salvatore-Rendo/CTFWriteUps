## Challenge Name: Web technologies: External Resources
**Category:** Web

**Challenge Description:**

A web page can contain references to other resources, called external, which increase it in terms of functionality, style, availability of fonts and more. The two main mechanisms for including these resources are the ```<link>``` tags, which specify the type of relationship with the external resource in the rel attribute (typically stylesheet or alternate stylesheet) and the address of the resource in href, and the ```<script>```, which in addition to directly containing a piece of code can link to external scripts via the src attribute.

In this challenge the flag is in one of the external resources of the page accessible at http://web-15.challs.olicyber.it/. 
### Approach

As descripted in the challenge description to solve this challenge is necessary to find the flag inside the external resources of the server.

The solution to this challenge is this [script](/olicyber-training/web/15-Extract-external-resources/solve.py):

```
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import requests

# URL of the target website
url = 'http://web-15.challs.olicyber.it/'

# Send a GET request to the website
response = requests.get(url)
html_text = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_text, 'html.parser')

# Find all external resources using <link> and <script> tags
external_resources = []

# Find external resources specified in <link> tags
link_tags = soup.find_all('link', {'rel': ['stylesheet', 'alternate stylesheet']})
for link_tag in link_tags:
    href = link_tag.get('href')
    if href:
        # Make the URL absolute if it's relative
        href = urljoin(url, href)
        external_resources.append(href)

# Find external resources specified in <script> tags
script_tags = soup.find_all('script', {'src': True})
for script_tag in script_tags:
    src = script_tag.get('src')
    if src:
        # Make the URL absolute if it's relative
        src = urljoin(url, src)
        external_resources.append(src)

# Iterate through external resources and search for the flag
for resource_url in external_resources:
    try:
        resource_response = requests.get(resource_url)
        resource_text = resource_response.text
        if 'flag{' in resource_text:
            flag = resource_text.split('flag{')[1].split('}')[0]
            print(f'flag{{{flag}}}')
            break
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resource at {resource_url}: {e}")

if 'flag' not in locals():
    print('Flag not found in any external resources.')

```

**Flag**

```
flag{5n00ping_4r0und}
```
### Reflections
Medium difficulty starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
