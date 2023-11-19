## Challenge Name: CHAOS
**Category:** Network

**Challenge Description:** 
Hello mortal, this is a communication from the world of c-h-a-o-s (yes, we have computers here too). will you be able to decipher it?


**Artifact Files:**
* [Pcap](/olicyber-training/network/Chaos/artifacts/CHAOS.pcap)
* [Extracted Json](/olicyber-training/network/Chaos/artifacts/packets.json)

### Approach

Trying to understand the traffic was not easy, I found that inside each TCP packets, the field 'TCP PAYLOAD' was always 1 or 0 byte that changed for each packet so i decided to extract the traffic as a json to analyze better the data.

**1 Extract the traffic to a json**

![img](</olicyber-training/network/Chaos/images/img1.png>)

**2. Extract the 'tcp.payload' field for each packet, analyze it and convert it to characters**

I have made a [script](/olicyber-training/network/Chaos/solve.py) in python to do this.

```
import json

# Load the JSON file
with open('olicyber-training/network/Chaos/artifacts/packets.json', 'r') as file:
    data = json.load(file)

# Extract tcp.payload from each packet, handling the case where the key might not exist
payload_list = [packet['_source']['layers']['tcp'].get('tcp.payload', '') for packet in data]

# Convert hex values to decimal and then to ASCII characters
ascii_characters = ''.join([chr(int(data, 16)) for data in payload_list if data])

# Print or process the ascii_characters as needed
print(ascii_characters)
```

**3. Reconstruct the flag from the analyzed payload or the output of the script**

```
Hl00
Ma}0U54HCT_f_C{g
```

**Flag** 
```
flag{T00_MUCH_CH405}
```

### Reflections
Fun challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
