## Challenge Name: HTTP: Option Method
**Category:** Web

**Challenge Description:** 

To find out the operations supported by a given resource, HTTP provides the OPTIONS verb. An OPTIONS request returns the list of supported verbs within the Allow header.

The objective of this challenge is to determine the set of supported verbs for the resource http://web-10.challs.olicyber.it/, try to use an uncommon and unexpected one and observe the response. The requests library provides functions similar to the get function also for less common verbs, such as put and patch.

### Approach

Create a POST request with the correct credential in json format and analyze its response with python with the following [script](/olicyber-training/web/10-Option/solve.py):

```
import requests

url = ' http://web-10.challs.olicyber.it/'

#r = requests.options(url=url)
r = requests.put(url=url)

print(r.headers)
```

```
{'Content-Length': '21', 'Content-Type': 'text/plain; charset=utf-8', 'Date': 'Fri, 17 Nov 2023 22:11:35 GMT', 'Server': 'nginx/1.21.6', 'X-Flag': 'flag{br34king_7h3_ru135}'}
```

**Flag**

```
flag{br34king_7h3_ru135}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
