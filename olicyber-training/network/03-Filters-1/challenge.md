## Challenge Name: Filters 1
**Category:** network


**Challenge Description:** 
This is the first of a series of challenges that will address the use of expressions to filter pcap/pcapng files, in order to obtain a reduced and more interesting set of packets.

To obtain the flag of this first challenge it is sufficient to filter the packets based on the protocol, in particular by filtering only the packets that use the HTTP protocol you will find the flag in a customized header of the request.

To best learn how to solve this series of challenges, it is recommended to read the relevant Wireshark documentation regarding filters.

**Artifact Files:**
* [Pcap](/olicyber-training/network/03-Filters-1/artifacts/nw-intro03.pcapng)


### Approach

**1. Apply HTTP only traffic Filter**

![img](</olicyber-training/network/03-Filters-1/images/img1.png>)

**2 Search inside the HTTP Header the flag**

```
flag{L3aRn1N9_4b0uT_F1lter5_p1}
```


### Reflections
Easy starting challenge
  

---
[Back to home](<link>){: .btn}
