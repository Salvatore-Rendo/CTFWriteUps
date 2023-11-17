## Challenge Name: HTTP: HEAD Method
**Category:** Web

**Challenge Description:** 

Sometimes it can be interesting for a client to know the metadata of a resource without necessarily having to receive the entire representation (think for example of the case of a large file). Precisely for these cases, the HTTP protocol provides the HEAD verb, designed to obtain the headers of an equivalent GET request in response, but without carrying out the transfer of the resource.

The reported headers should be identical to those of a similar GET request but, as in the case of the Accept header, a faulty or misconfigured server can accidentally leak additional information that would not be included in the response to a normal GET request.

The objective of this challenge is to perform a HEAD request to the resource http://web-07.challs.olicyber.it/ and observe the returned headers.
### Approach

Create a HEAD request and analyze its headers with python with the following [script](/olicyber-training/web/07-head-method/solve.py):

```
import requests

url = 'http://web-07.challs.olicyber.it/'

r = requests.head(url=url)

print(r.headers)
```
The following server response leaks the flag inside the HEAD request headers:

```
{'Content-Length': '12', 'Content-Type': 'text/plain; charset=utf-8', 'Date': 'Fri, 17 Nov 2023 19:58:29 GMT', 'Server': 'nginx/1.21.6', 'X-Flag': 'flag{r0gu3_m374d474}'}
```

**Flag**

```
flag{r0gu3_m374d474}
```
### Reflections
Easy starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
