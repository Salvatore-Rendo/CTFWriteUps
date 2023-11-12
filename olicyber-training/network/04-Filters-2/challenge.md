## Challenge Name: Filters 2
**Category:** Network

**Challenge Description:** 
To solve this challenge, a logical expression is needed that filters by source IP address (192.168.100.3) and by protocol (DNS).

**Artifact Files:**
* [Pcap](/olicyber-training/network/03-Filters-1/artifacts/nw-intro03.pcapng)

### Approach

**1. Filter the right traffic using the following filter:**
```
dns && ip.addr==192.168.100.3
```


![img](</olicyber-training/network/04-Filters-2/images/img1.png>)

**2 Search inside the DNS Query field to get the flag.**

```
flag{L3aRn1N9_4b0uT_F1lter5_1P_DN5_f1lt3r}
```


### Reflections
Easy starting challenge.
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
