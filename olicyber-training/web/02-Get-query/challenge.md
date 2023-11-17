## Challenge Name: HTTP: GET request with query string
**Category:** Web

**Challenge Description:** 
The request for some resources can be parameterized, to obtain particular versions of the resource in question. For example, a blog could use a single resource to represent all published posts (which are all structurally the same, differing only in content) by identifying the specific content desired via a numeric id parameter.

The objective of this challenge is to obtain the resource http://web-02.challs.olicyber.it/server-records by specifying the id parameter with the flag value.


### Approach


Make a request with the browser at the defined URL

```http://web-02.challs.olicyber.it/server-records?id=flag```

Or do it with python with the following [script](/olicyber-training/web/02-Get-query/solve.py):

```
import requests

query = {'id' : 'flag'}

r = requests.get(url='http://web-02.challs.olicyber.it/server-records', params=query)

print(r.text)
```

**Flag**

```
flag{wh47_i5_y0ur_qu3ry}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
