## Challenge Name: Stream TCP
**Category:** Network

**Challenge Description:** 

This challenge focuses on TCP conversations (TCP Streams).

The flag is divided character by character into different TCP packets belonging to the same session.

Since the pcap file is large and also contains many scattered ICMP packets, the most efficient solution is to filter the session of interest and view it in full.

**Artifact Files:**
* [Artifact1](/olicyber-training/network/07-StreamTCP/artifacts/nw-intro07.pcapng)


### Approach

**1.  Filter the right traffic using the following filter:**

```
tcp.stream
```

![img](</olicyber-training/network/07-StreamTCP/images/img1.png>)

**2 Follow the tcp stream and get the flag inside**

![img](</olicyber-training/network/07-StreamTCP/images/img2.png>)

**Flag:**
```
flag{F0lloW_7h3_Wh1t3_5tr3aM_4l1c3}
```


### Reflections
Easy starting challenge
  

---
[Back to home](<link>){: .btn}
