## Challenge Name: HTTP: POST request with json body
**Category:** Web

**Challenge Description:** 

The objective of this challenge is to send a POST request to the resource http://web-09.challs.olicyber.it/login providing the pair of "username" values: "admin" and "password" in JSON format: " admin", similarly to a hypothetical login operation towards a web service. The flag will be returned in the response text to the operation.

### Approach

Create a POST request with the correct credential in json format and analyze its response with python with the following [script](/olicyber-training/web/09-Post-json/solve.py):

```
import requests

url = 'http://web-09.challs.olicyber.it/login'
post = {'username':'admin', 'password':'admin'}

r = requests.post(url=url,json=post)

print(r.text)
```

```
{
  "token": "flag{w31c0m3_70_7h3_y34r_2000}"
}
```

**Flag**

```
flag{w31c0m3_70_7h3_y34r_2000}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
