## Challenge Name: Wordwang
**Category:** Network

**Challenge Description:** 
After the spectacular success of NumberWang we are here with a new edition of the favorite game of people aged 25 to 25 and a half: WordWang! Will you be able to get the WordWang?

You can connect to the remote service with:

```nc wordwang.challs.olicyber.it 10601```


**Artifact Files:**
* [Pcap](/olicyber-training/network/Cat/artifacts/G4tt0.pcapng)


### Approach

**1. Filter the traffic and follow the TCP Stream**

![img](</olicyber-training/network/Wordwang/images/img1.png>)

**2. After loking up the traffic is possible to understand the server flow**

The server gives you a word, and to get the flag you must send:

```?GIVEN_WORD!```

![img](</olicyber-training/network/Wordwang/images/img2.png>)

**3. Connect to the server and get the flag**

![img](</olicyber-training/network/Wordwang/images/img3.png>)

**Flag** 
```
flag{n1c3_0n3_jul13!Th4ts_w0rdw4ng!}
```

### Reflections
Easy challenge
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
