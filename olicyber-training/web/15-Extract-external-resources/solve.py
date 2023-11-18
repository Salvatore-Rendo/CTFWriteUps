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
