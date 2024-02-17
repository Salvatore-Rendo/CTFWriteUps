## Challenge Name: Rick Roller
**Category:** Web

**Challenge Description:**

They sent me this link but I keep getting redirected to a strange video. Can you tell me why?

Website: http://roller.challs.olicyber.it

### Approach

This site has a ```/get_flag.php``` page that redirects to a youtube video.

Blocking the redirect gives us the flag.

The solution to this challenge is this [script](/olicyber-training/web/Rick-Roller/solve.py):

```
import requests

r = requests.get(url='http://roller.challs.olicyber.it/get_flag.php',allow_redirects=False)

print(r.content)
```

or using [curl](https://curl.se/) inside a terminal.

```
curl http://roller.challs.olicyber.it/get_flag.php
```



**Flag**

```
flag{r1ck_4st1ey_c14ssic_m3m3}
```
### Reflections
Easy difficulty challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
