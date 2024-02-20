## Challenge Name: Password Changer 3000
**Category:** Web

**Challenge Description:**

Can you change the password of the "admin" user?

Site: http://password-changer.challs.olicyber.it

### Approach

Inside the challenge's site it's possible to change the password by giving a username as input inside a form 

For example giving the username ```'username123'``` will change the password of that given credential.

I noticed that inside the request URL to ```/change-password.php``` is present the token of the request: 
```
http://password-changer.challs.olicyber.it/change-password.php?token=dXNlcm5hbWUxMjM=
```

The token ```dXNlcm5hbWUxMjM=``` is just the ```'username123'``` encodedin Base64.

So to change the admin password you need to give the following token ("admin" in Base64) inside the URL:

```
YWRtaW4=
```
```
http://password-changer.challs.olicyber.it/change-password.php?token=YWRtaW4=
```

**Flag**

```
flag{0h_n0_y0u_c4n_m0d1fy_urls}
```
### Reflections
Easy difficulty challenge 
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
