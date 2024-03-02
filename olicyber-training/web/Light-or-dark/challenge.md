## Challenge Name: Light or Dark
**Category:** Web

**Challenge Description:**

A simple website that lets you choose between light, dark, and… nah, just these two.
PS: PHP version: 4

Website: http://lightdark.challs.olicyber.it

### Approach

The challenge 
```
<?php

if(!isset($_GET["tema"])) $path = "light.css";  // Default
else {
    $path = $_GET["tema"];
    if (preg_match("/..\//", $path)) {  // Non è bene andare in giro per il file system..
        $path = str_replace('../', './' , $path);
        
        // Facciamo un filtro sull'estensione del tema richiesto, giusto per sicurezza c:
        $error = false;
        $arr = explode(".", $path);
        $estensione = $arr[count($arr)-1];

        if($estensione != "css"){
            $error = true;
            $path = substr($path, 0, -3) . "css";
        }
    }
}

$css = "static/css/" . $path;

?>


<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>L/D</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <style>
        <?php echo file_get_contents($css); ?>
    </style>

    <!-- Bootstrap JavaScript -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </head>

  <body>
    <div class="text-center my-3">
        <h1>Selettore di tema: Light & Dark</h1>
        <p class="pt-3" style="font-size:23;">
            <i>Hai mai sognato di poter cambiare il tema con un semplice click? Finalmente puoi!</i>
        </p>
    </div>

    <div class="row mt-5 w-100">
        <div class="col-2 col-md-4"> </div>
        <div class="col text-center">
            <button class="p-2" onclick="window.location.href='index.php?tema=light.css'">Tema chiaro</button>
        </div>
        <div class="col text-center">
            <button class="p-2" onclick="window.location.href='index.php?tema=dark.css'">Tema scuro</button>
        </div>
        <div class="col-2 col-md-4"> </div>
    </div>

    <div class="error mt-5 text-center">
        <?php if($error) echo "<img src='static/img/zeb.jpg' style='width: 50vw;'/>"; ?>
    </div>

  </body>
</html>
``` 

By looking at the php code i found 2 different steps to bypass:
- Directory Traversal filter
- File extension check

Following there is the solution of this challenge and immediately after there is the explanation of the choices made.
```
http://lightdark.challs.olicyber.it/index.php?tema=.../.../.../.../.../flag.txt%00.css
```

#### Directory Traversal with .../ and null byte %00

In the PHP script provided, there's a vulnerability in how the $path variable is constructed based on the tema parameter from the URL. The code uses ../ to navigate up one directory level from the static/css/ directory. However, since the code replaces ../ with ./, it effectively nullifies the attempt to traverse directories.

To bypass this check, we can use .../ instead of ../. The PHP script will replace .../ with ./, leaving ../ intact. 


By appending %00 (null byte) at the end of a string in a URL exploits PHP's interpretation of null bytes to truncate the string. PHP treats null bytes as string terminators, effectively ignoring any characters after them.

In this challenge, appending %00.css to the tema parameter ensures that the file extension check in the PHP script fails to recognize the actual file extension. This bypasses the validation and allows an attacker to access files with arbitrary extensions, including sensitive files such as flag.txt.

By combining the use of .../ for directory traversal and %00 for bypassing file extension checks, attackers can effectively exploit the vulnerability and access sensitive files on the server.


**Flag**

```
flag{l1ght_1s_f0r_n00bs_d4rk_1s_f0r_h4ck3rs}    
```
### Reflections
Easy difficulty challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
