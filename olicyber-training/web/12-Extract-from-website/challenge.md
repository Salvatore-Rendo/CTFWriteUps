## Challenge Name: Web technologies: extract simple content from a web page
**Category:** Web

**Challenge Description:** 

The primary use of HTTP remains to transport hypertext documents commonly known as web pages. These documents are described using the HTML markup language and can have a fairly complex structure. Fortunately, numerous libraries are available that can be used to extract the data they contain, which eliminate the difficulty of having to interpret such a complex format.

Hypertexts are basically text documents, portions of which are delimited by pairs of identifiers, called tags, which specify their function within the page. For example, a paragraph will be delimited by a ```<p> ... </p>``` pair, a link by ```<a> ... </a>```, and so on. These tags can also contain additional information, called attributes, that define characteristics of the delimited text (for example, the destination of a link is specified in the href Hypertext REFerence attribute of the ```<a>``` tag)

In this challenge the flag is contained in the second paragraph of the web page accessible at the URL http://web-12.challs.olicyber.it/.

### Approach

As descripted in the challenge description to solve this challenge is necessary to get the flag from the second paragraph of the given website html page.

The solution to this challenge is this [script](/olicyber-training/web/12-Extract-from-website/solve.py):

```
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
```

**Flag**

```
flag{7h3_14ngu4g3_0f_7h3_w3b}
```
### Reflections
Easy difficulty starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
