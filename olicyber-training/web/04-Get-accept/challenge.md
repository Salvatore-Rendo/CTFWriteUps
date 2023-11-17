## Challenge Name: HTTP: The Accept header
**Category:** Web

**Challenge Description:** 

The objective of this challenge is to request the resource http://web-04.challs.olicyber.it/users using the alternative application/xml representation instead of the default application/json one.

We recommend trying to get the resource normally, and then specifying a different representation type (application/xml) via the Accept header.

### Approach

Create a request with the accept header set to application/xml with python with the following [script](/olicyber-training/web/04-Get-accept/solve.py):


```
import requests

header = {'accept' : 'application/xml'}

url = 'http://web-04.challs.olicyber.it/users'

r = requests.get(url=url,headers=header)

print(r.text)
```
The response of the server is the following:

```
<?xml version="1.0"?>

<users>
  <user comment="flag{54m3_7hing_diff3r3n7_7hing}">
    <name>admin</name>
    <role>admin</role>
    <registration_date>2018-06-18T15:34:55Z</registration_date>
  </user>
  <user>
    <name>fruitfly</name>
    <role>user</role>
    <registration_date>2019-08-12T12:04:32Z</registration_date>
  </user>
  <user>
    <name>jim87</name>
    <role>user</role>
    <registration_date>2022-01-13T20:09:43Z</registration_date>
  </user>
  <user comment="Suspicious activity">
    <name>anonymous05</name>
    <role>user</role>
    <registration_date>2022-03-09T16:01:07Z</registration_date>
  </user>
</users>

```

**Flag**

```
flag{54m3_7hing_diff3r3n7_7hing}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
