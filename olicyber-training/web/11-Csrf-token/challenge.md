## Challenge Name: HTTP: CSRF Tokens
**Category:** Web

**Challenge Description:** 

The CSRF token is a system used to prevent the execution of Cross-Site Request Forgery attacks. The attack would consist of tricking a user of a web service into clicking on a link or the submit button of a form included in an email or on a site controlled by the attacker, which targets a "dangerous" resource of the target service (e.g. a resource whose request represents an account deletion command). The session cookie mechanism, which can only be obtained with a username and password unknown to the attacker, prevents the latter from personally carrying out the "dangerous" operation by impersonating the user, but if the user is deceived into click the malicious link on a machine on which you have previously accessed the target service, the cookie containing the session token will be automatically attached to the request made, validating it, without the attacker needing to steal it or reproduce a counterfeit one.

The CSRF token prevents this type of attack because it is not sent automatically by the browser like normal cookies. It is however stored on the client machine in a storage accessible only to the resources associated with the relevant service (and therefore out of the attacker's control), but must be explicitly attached to HTTP requests in the form, for example, of a GET parameter, or to inside the body of a POST request, when they are executed. In this way it is impossible to get the user to generate a dangerous request with a simple click, because to generate a dangerous link the attacker would be forced to know the token. To further complicate matters, CSRF tokens are typically disposable, and with each successful operation the client receives a new one randomly generated. The new token is usually added to the body of the returned resource.

In this challenge, the flag is divided into four pieces, accessible via the resource http://web-11.challs.olicyber.it/flag_piece based on the index parameter. To access it, you must have previously sent a POST login request to the resource http://web-11.challs.olicyber.it/login, with a JSON body containing "username": "admin" and "password": "admin" , and having received a session cookie in exchange. In addition to the session token in the cookie, the login resource will also return a CSRF token in the response body (also JSON). For each correctly executed request the client will receive a new token to use for the next one.

### Approach

As descripted in the challenge description to solve this challenge is necessary to get all the flag pieces after getting the session cookis from the "login" resource and the right use of the CSRF TOKENS at each GET request to the "flag_piece" resource

The solution to this challenge is this [script](/olicyber-training/web/11-Csrf-token/solve.py):

```
import requests

#Log in to get coockies
url_credentials = 'http://web-11.challs.olicyber.it/login'

s = requests.Session()

body = {'username':'admin', 'password':'admin'}

r = s.post(url=url_credentials,json=body)

#Extract session cookie and csrf token
session_coockie = r.cookies

csrf_value = r.json()['csrf']

url_flag='http://web-11.challs.olicyber.it/flag_piece'

flag = ''

#extract the flag pieces using session cookie and
# csrf token that change at every get to the resource
for i in range(4):

    r = s.get(url=(url_flag+'?csrf='+csrf_value+'&index='+str(i)),
            cookies=session_coockie)
    
    csrf_value = r.json()['csrf']

    flag_piece = r.json()['flag_piece']
    
    flag = flag + flag_piece
    
print(flag)
```

**Flag**

```
flag{v3ry_53ri0u5_53ri35_0f_r3qu3575}
```
### Reflections
Medium difficulty starting challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
