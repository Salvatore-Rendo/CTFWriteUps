## Challenge Name: HTTP: POST request
**Category:** Web

**Challenge Description:** 
In principle the representation of the resource sent in the body of a POST request can use any format but, for historical reasons, when using the browser's built-in sending mechanism to send the contents of a form, this is normally encoded using a specific legacy format used exclusively for web forms, known in MIME classification as application/x-www-form-urlencoded. For this reason, many servers that receive data from users via POST requests preferentially accept this format, even when the data source is not a web form.

The objective of this challenge is to send a POST request to the resource http://web-08.challs.olicyber.it/login providing the value pair in the application/x-www-form-urlencoded format "username": "admin" and "password": "admin", similarly to a hypothetical operation of sending a login form on a website. The flag will be returned in the response text to the operation.

### Approach

Create a POST request and analyze its response with python with the following [script](/olicyber-training/web/08-Post/solve.py):

```
import requests

url = 'http://web-08.challs.olicyber.it/login'
post = {'username':'admin', 'password':'admin'}

r = requests.post(url=url,data=post)

print(r.text)
```



**Flag**

```
flag{53nding_d474_7h3_01d_w4y}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
