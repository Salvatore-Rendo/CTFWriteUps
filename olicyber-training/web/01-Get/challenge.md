## Challenge Name: HTTP: A simple GET request
**Category:** Web

**Challenge Description:** 
Conceived to facilitate access to hypertext documents, the HyperText Transfer Protocol HTTP is now used to transfer information of all types to and from remote servers across the network. This information is organized into resources, identified by address strings called URLs (Unified Resource Locators), and the fundamental operations that can be performed on these resources are called HTTP verbs.

The simplest of these verbs, GET, is used to get a resource from a remote server. The objective of this challenge is to obtain the text of the root resource of the server web-01.challs.olicyber.it, identified by the URL http://web-01.challs.olicyber.it/


### Approach


Make a request with the browser at the defined URL or do it with python with the following [script](/olicyber-training/web/01-Get/solve.py):

```
import requests

r = requests.get(url='http://web-01.challs.olicyber.it/')

print(r.text)
```

**Flag**

```
flag{g3t7ing_4l0ng}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
