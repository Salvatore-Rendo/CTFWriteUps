## Challenge Name: Filters 4
**Category:** Network

**Challenge Description:** 
To solve this challenge, a logical expression is needed that filters to select only packets containing the string "Pwn all the things!!!".

The flag will then be formatted as per standard: flag{...}.
**Artifact Files:**
* [Pcap](/olicyber-training/network/03-Filters-1/artifacts/nw-intro03.pcapng)

### Approach

**1. Filter the right traffic using the following filter:**
```
data.data contains "Pwn all the things!!!"
```
OR
```
data contains "Pwn all the things!!!"
```
Both of these filters are valid, but the first one (data.data contains "Pwn all the things!!!") is more precise in targeting the payload data.

![img](</olicyber-training/network/06-Filters-4/images/img1.png>)

**2 Search inside the comment field to get hex data**

```
50776e20616c6c20746865207468696e67732121212074686520666c34672069733a204c3361526e314e395f34623075545f46316c746572355f46316e645f54683073335f537472316e36355f6d380a
```

**3 Convert it and get the flag**

```
Pwn all the things!!! the fl4g is: L3aRn1N9_4b0uT_F1lter5_F1nd_Th0s3_Str1n65_m8
```

**Flag:**
```
flag{L3aRn1N9_4b0uT_F1lter5_F1nd_Th0s3_Str1n65_m8}
```


### Reflections
Easy starting challenge.
  

---
[Back to home](</olicyber-training/main.md>){: .btn}
