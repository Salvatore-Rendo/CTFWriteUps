## Challenge Name: PocaCola Recipe
**Category:** Network

**Challenge Description:** 
I've been hiding under a table in Poca Cola headquarters for 3 days, I've tracked all their communications! Please find the secret recipe so I can get out of here...


**Artifact Files:**
* [Pcap](/olicyber-training/network/PocaCola-recipe/artifacts/intercepted.pcap)
* [Zipped Recipe](/olicyber-training/network/PocaCola-recipe/artifacts/download.zip)

### Approach

**1. Filter the traffic to finde the packets containing uploaded files**

```http.request.method == "POST"```

![img](</olicyber-training/network/PocaCola-recipe/images/img1.png>)

**2. After looking up the uploaded files, i found a suspicoius .zip file in frame 18626, but a password is required to unzip it**

![img](</olicyber-training/network/PocaCola-recipe/images/img2.png>)

**3. Filter the traffic searching for a password and follow the TCP stream**

```data contains "password"```

![img](</olicyber-training/network/PocaCola-recipe/images/img3.png>)

**4. Use the password to unzip the recipe and get the flag**

**Flag** 
```
flag{l'1n6r3d13n73_536r370_è_am0r3..e_p4t4t3}
```

### Reflections
Fun challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
