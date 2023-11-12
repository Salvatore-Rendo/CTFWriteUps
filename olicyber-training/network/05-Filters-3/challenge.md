## Challenge Name: Filters 3
**Category:** Network

**Challenge Description:** 
To solve this challenge you need a logical expression that filters to find packets containing comments.

**Artifact Files:**
* [Pcap](/olicyber-training/network/03-Filters-1/artifacts/nw-intro03.pcapng)

### Approach

**1. Filter the right traffic using the following filter:**
```
frame.comment
```

Or go to **Anlyze > Expert information** and go to the packet with a comment.


![img](</olicyber-training/network/05-Filters-3/images/img1.png>)

**2 Search inside the comment field to get the flag.**

```
flag{L3aRn1N9_4b0uT_F1lter5_C0mm3Nt5_4R3_H4rd_t0_f1nD}
```


### Reflections
Easy starting challenge.
  

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>