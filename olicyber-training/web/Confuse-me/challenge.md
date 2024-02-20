## Challenge Name: Confuse me
**Category:** Web

**Challenge Description:**

You can try to confuse me, but, sorry, you're not the right guy for me.

Website: http://confuse-me.challs.olicyber.it

### Approach

This challenge expose the php source code: 



```
<?php

if (isset($_GET["s"])) {
  highlight_file("index.php");
  exit;
}

$flag = getenv("FLAG");

echo "
<html>
<body>
  <form>
  Input: <input name=input />
  </form>

  <a href='?s'>Sorgente disponibile qui</a>.<br/>
</body>
</html>
";

if (isset($_GET['input'])) {
  $user_input = $_GET['input'];
      
  if ($user_input == substr(md5($user_input), 0, 24)) {
    echo "Ce l'hai fatta! Ecco la flag: $flag";
  } else {
    echo "Nope nope nope";
  }
}
```

The relevant part of the source code is:

```
if ($user_input == substr(md5($user_input), 0, 24)) 
```

Regarding the ```==``` php operator this [README](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md) explains how this check can be bypassed thanks to the php Type Juggling and the Magic numbers/string regarding MD5 encryption.

Using this payload as user input will lead to bypass the ```==``` check and get the flag:

```
0e215962017
```


**Flag**

```
flag{0mg_php_c0mp4r150n_r34lly_5uck5}
```
### Reflections
Easy difficulty challenge (once you find the vulnerabilty)
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
