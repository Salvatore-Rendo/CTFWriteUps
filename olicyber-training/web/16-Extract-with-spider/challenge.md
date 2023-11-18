## Challenge Name: Web technologies: a simple spider
**Category:** Web

**Challenge Description:**

The fundamental characteristic of a hypertext is that its pages contain hyperlinks to other pages, in a network of mutual references called the Web.

In this challenge a network of pages can be reached via the URL http://web-16.challs.olicyber.it/. The flag is contained within the title ```(<h1>)``` of one of these pages. The objective is to automatically traverse the network of pages until reaching the one containing the flag.

It is recommended to use the find_all method of the BeautifulSoup library to isolate the ```<a>``` tags and extract the destination address from the href attribute, and to maintain a set of visited pages so as not to analyze them more than once, to avoid creating load to the server being analyzed unnecessarily and to remain trapped in an infinite loop if two or more pages were to link to each other.

Further information: software that explores a network of pages by following all the hyperlinks is called a spider, and is a fundamental component of modern search engines.
### Approach

As descripted in the challenge description to solve this challenge is necessary to find the flag inside the external resources of the server.

I have not searched for the ```<h1>``` title because i wanted to create a generic spider reusable for other challenges.

The solution to this challenge is this [script](/olicyber-training/web/16-Extract-with-spider/solve.py):

```
import requests
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin

def find_flag_in_text(text):
    # Find the first occurrence of 'flag{...}' in the given text, including comments
    soup = BeautifulSoup(text, 'html.parser')
    for element in soup.find_all(string=True):
        if isinstance(element, Comment):
            continue  # Skip comments
        flag_start = element.find('flag{')
        if flag_start != -1:
            flag_end = element.find('}', flag_start)
            if flag_end != -1:
                return element[flag_start:flag_end + 1]
    return None

def spider(url):
    visited_pages = set()
    to_visit = [url]

    while to_visit:
        current_url = to_visit.pop(0)

        if current_url in visited_pages:
            continue

        try:
            response = requests.get(current_url)
            html_text = response.text

            # Check if the flag is present in the HTML text
            flag = find_flag_in_text(html_text)
            if flag:
                print(f'{flag}')
                return

            visited_pages.add(current_url)

            # Extract links from the current page
            soup = BeautifulSoup(html_text, 'html.parser')
            link_tags = soup.find_all('a', href=True)
            new_links = [urljoin(current_url, link['href']) for link in link_tags]

            # Add unvisited links to the to-visit list
            to_visit.extend(link for link in new_links if link not in visited_pages and link not in to_visit)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page at {current_url}: {e}")

    print('Flag not found in any visited pages.')

if __name__ == "__main__":
    starting_url = 'http://web-16.challs.olicyber.it/'
    spider(starting_url)
```

**Flag**

```
flag{n0wh3r3_i5_54f3}
```
### Reflections
Medium difficulty starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
