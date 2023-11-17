## Challenge Name: HTTP: Receive a cookie
**Category:** Web

**Challenge Description:** 

The objective of this challenge is to perform a GET request to the resource http://web-06.challs.olicyber.it/token which will try to install a session cookie, once obtained which it will be possible to access http://web-06.challs.olicyber.it/flag to obtain the flag.

### Approach

Create a session making multiple requests with python with the following [script](/olicyber-training/web/06-recive-cookie/solve.py):


```
import requests

url_token = 'http://web-06.challs.olicyber.it/token'
url_flag = 'http://web-06.challs.olicyber.it/flag'

s = requests.session()

s.get(url=url_token)

r = s.get(url=url_flag)

print(r.text)
```

**Flag**

```
flag{7w0_574g3_4cc3s5}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
