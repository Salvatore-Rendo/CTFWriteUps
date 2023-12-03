## Challenge Name: O Data, All Ye Faithful 
**Category:** Log Analysis


**Challenge Description:** 
After yesterday’s resounding success, McHoneyBell walks into AntarctiCrafts’ office with a gleaming smile. She takes out her company-issued laptop from her knapsack and decides to check the news. “Traffic on the North-15 Highway? Glad I skied into work today,” she boasts. A notification from the Best Festival Company’s internal communication tool (HollyChat) pings.

It’s another task. It reads, “The B-Team has been tasked with understanding the network of AntarctiCrafts’ South Pole site”. Taking a minute to think about the task ahead, McHoneyBell realises that AntarctiCrafts has no fancy technology that captures events on the network. “No tech? No problem!” exclaims McHoneyBell.

**Use the provided Jupyter Notebooks session to analyze the "network_traffic.csv"**

**Artifact Files:**
* None

### Approach

**1.How many packets were captured?**
After importing pandas and matplotlib libraries and reading the .csv file with:
```df = pd.read_csv('network_traffic.csv')```

![img](</advent-of-cyber/data-faithful/images/img1.png>)

It's possible to retrive the packets logged inside the file with:
```df.count()```

![img](</advent-of-cyber/data-faithful/images/img2.png>)


```100``` is the answer.    

**2 What IP address sent the most amount of traffic during the packet capture?**

To retrive the Ip address that sent the most amount of packets we can use the groupby() funcion in conjuntion with the size() function:
```df.groupby(['Source']).size()```


![img](</advent-of-cyber/data-faithful/images/img3.png>)

IP Address: ```10.10.1.4``` with 15 packets.

**3.What was the most frequent protocol?**

For the most frequent protocol used inside the packet capture we can use again the groupby() and size() functions:
```df.groupby(['Protocol']).size()```



![img](</advent-of-cyber/data-faithful/images/img4.png>)

Protocol: ```ICMP``` with 27 packets.




### Reflections
Easy challenge
  

---
<a href="/advent-of-cyber/main.md" class="btn">Back to home</a>
