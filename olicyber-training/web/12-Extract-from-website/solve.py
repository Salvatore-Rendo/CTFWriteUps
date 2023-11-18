import requests
from bs4 import BeautifulSoup

url = 'http://web-12.challs.olicyber.it/'

r  = requests.get(url=url)

html_text = r.text

#open the html body with bs4
soup =  BeautifulSoup(html_text, 'html.parser')

#get the second paragraph content
flag = soup.find_all("p")[1].text

print(flag)