## Challenge Name: Make a Wish
**Category:** Web

**Challenge Description:**

I created the perfect blacklist! No one will be able to bypass it, I used a regex that filters out literally everything.

Website: [http://make-a-wish.challs.olicyber.it](http://make-a-wish.challs.olicyber.it)

### Approach

The provided PHP code includes a regular expression check to filter input. The code snippet checks if a parameter named `richiesta` exists in the URL and then applies a regular expression pattern `/ . * / i` (which matches any string) to the value of the `richiesta` parameter.

```php
<?php
if(isset($_GET['richiesta'])) {
  if (preg_match("/.*/i", $_GET['richiesta'], $match))  {
    echo "No, mi dispiace non posso fare questo!";
  } else {
    echo "flag{TROVAMI}";
  }
} else {
  echo "Fai una richiesta e provero a realizzarla";
}
?>
```

To bypass the filter, we exploit how PHP interprets array parameters in the URL. By sending `richiesta[]=`, we pass an array parameter instead of a string. This happens because the function is designed to operate on strings, not arrays. As a result, the denial message is not triggered, and the flag is revealed.

So the solution to this challenge is: 

```
http://make-a-wish.challs.olicyber.it?richiesta[]=
```

**Flag**
flag{r3g3x_byp455_php_5tyl3}  

### Reflections

This challenge highlights the importance of understanding how PHP interprets and handles parameters in URLs, especially when dealing with array parameters. By exploiting PHP's behavior regarding array parameters and regular expression filtering, we were able to bypass the supposed "perfect" blacklist and obtain the flag.

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>


