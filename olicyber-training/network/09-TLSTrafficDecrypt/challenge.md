## Challenge Name: <name>
**Category:** <category>
**Points:** <points>
**Solves:** <number>

**Challenge Description:** 
<descript>

**Artifact Files:**
* [Pcap](/olicyber-training/network/09-TLSTrafficDecrypt/artifacts/nw-intro09.pcapng)
* [TLS Keys Log File](/olicyber-training/network/09-TLSTrafficDecrypt/artifacts/tls-keys.txt)

### Approach

**1. Use the keys inside the key log file to decrypt the tls data**

To add the keys: **Edit > Preferences > Protocols > TLS** and add the key log file inside the "(PRE)-Master-Secret log filename" field.

![img](</olicyber-training/network/09-TLSTrafficDecrypt/images/img1.png>)

**2. Filter to only see the TLS decrypted traffic and get the flag from the GET request Header**

Use the ```tls``` filter to see the decrypted traffic, look up the GET / request Headers to find the flag.

![img](</olicyber-training/network/09-TLSTrafficDecrypt/images/img2.png>)

**Flag:**
```
flag{S3cr3t_K3y5_4re_n0_J0k3}
```
### Reflections
Easy starting challenge
  

---
<a href="" class="btn">Back to home</a>
