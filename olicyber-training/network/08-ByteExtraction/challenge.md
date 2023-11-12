## Challenge Name: Byte Extraction
**Category:** Network

**Challenge Description:** 

This challenge focuses on analyzing and extracting the bytes of a given packet.

In this capture there is in fact a short exchange of TCP packets, in particular we are interested in the frame containing the data sent from the IP 192.168.100.1 to 192.168.100.2.

To obtain the flag it is necessary to extract the bytes of this packet and analyze its contents.

For further information, refer to the relevant documentation.

**Artifact Files:**
* [Pcap](/olicyber-training/network/08-ByteExtraction/artifacts/nw-intro08.pcap)


### Approach

**1.  Extract the TCP packets as a .json file**

Filter the packets with:
```
tcp.stream
```
Extract the traffic with a .json file:
![img](</olicyber-training/network/08-ByteExtraction/images/img1.png>)

**2. Extract the data.data field from one packet among the extracted packets**
```
1f8b0800710360620003edd1410ac2301085e1ac3d45bc80cc34895d2b788e1084ba110b698416e9dd0d821b115d1511fe6ff30666f398e9cee9b42963310b926aebfd23abd714f162d437ae4e1aa435a2daa8182b4b967aba0e25656b4deefb8f47f8b6ff535dfdff6d3f1517e2616cf3ee58542e5187e85298d6f3ead7fd0000000000000000000000000000efdd0148a5cfb900280000
```
**3. Get the flag.txt file**
After an analysis of what types of bytes, i found thaks to [CyberChef](https://gchq.github.io/CyberChef/) that those byte where a compressed file with both gzip and tar.
After the decompression you will get the **flag.txt** file containg the flag.

**Solving script**
I have created a [Python Script](/olicyber-training/network/08-ByteExtraction/solve/solve.py) that does all 3 steps, extracting the 'flag.txt' from the 'extraction.json' file:

```
import json
import gzip
import io
import binascii
import tarfile

json_path = 'olicyber-training/network/08-ByteExtraction/solve/extraction.json'

with open(json_path) as f:
    json_data = json.load(f)

# Extract the data.data field from each packet and store in a list
extracted_data = []

for packet in json_data:
    source_data = packet.get('_source', {})
    layers_data = source_data.get('layers', {})
    
    if 'data' in layers_data:
        data = layers_data.get('data', None)
        data_data = data.get('data.data', None)

        if data_data is not None:
            # Remove colons and convert hex string to bytes
            data_data = data_data.replace(":", "")
            extracted_data.append(data_data)

# Concatenate the extracted data into a single string
compressed_data = ''.join(extracted_data)

# Convert the hex string to bytes
compressed_bytes = binascii.unhexlify(compressed_data)

# Create a decompression object for gzip
with gzip.GzipFile(fileobj=io.BytesIO(compressed_bytes), mode='rb') as f:
    uncompressed_data = f.read()

# Check if the uncompressed data is a tar archive
try:
    with tarfile.open(fileobj=io.BytesIO(uncompressed_data), mode='r') as tar:
        # Extract all members of the tar archive
        tar.extractall('.')
        print("Tar archive extracted successfully.")
except tarfile.TarError:
    # If it's not a tar archive, assume it's a regular text file
    decoded_data = uncompressed_data.decode('utf-8')
    print(f"Decoded data:\n{decoded_data}")

```
Check the [solve folder](/olicyber-training/network/08-ByteExtraction/solve/) to see the file used to solve the challenge

**Flag:**
```
flag{Byt35_Ex7rAct10n_1s_3a5y!}
```


### Reflections
Medium-easy starting challenge
  

---
[Back to home](<link>){: .btn}
