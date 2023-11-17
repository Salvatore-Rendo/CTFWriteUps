## Challenge Name: HTTP: Manual cookie
**Category:** Web

**Challenge Description:** 

Among the information exchanged between client and server via HTTP headers are small pieces of information called cookies. Unlike non-standard headers, cookies are specifically designed by the HTTP standard to contain arbitrary data useful for the operation of sites and web services and are commonly used as part of additional authentication mechanisms to those offered by the standard.

Similar to challenge number 3, the objective is to obtain the resource http://web-05.challs.olicyber.it/flag by providing the admin string in a cookie named password.

### Approach

Create a request with the accept header set to application/xml with python with the following [script](/olicyber-training/web/05-cookie/solve.py):


```
import requests

cookie = {'password' : 'admin'}

#cookie = dict(password='admin')

url = 'http://web-05.challs.olicyber.it/flag'

r = requests.get(url=url,cookies=cookie)

print(r.text)
```



**Flag**

```
flag{v3ry_7457y_c00ki35}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
