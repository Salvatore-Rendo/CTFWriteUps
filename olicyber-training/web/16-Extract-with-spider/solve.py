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
