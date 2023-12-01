## Challenge Name: Chatbot, tell me, if you're really safe? 
**Category:** Machine Learning


**Challenge Description:** 
McHoneyBell and her team were the first from Best Festival Company to arrive at the AntarctiCrafts office in the South Pole. Today is her first day on the job as the leader of the "Audit and Vulnerabilities" team, or the "B Team" as she affectionately calls them.

In her mind, McSkidy's Security team have been the company's rockstars for years, so it's only natural for them to be the "A Team". McHoneyBell's new team will be second to them but equally as important. They'll operate in the shadows.

McHoneyBell puts their friendly rivalry to the back of her mind and focuses on the tasks at hand. She reviews the day's agenda and sees that her team's first task is to check if the internal chatbot created by AntarctiCrafts meets Best Festival Company's security standards. She's particularly excited about the chatbot, especially since discovering it's powered by artificial intelligence (AI). This means her team can try out a new technique she recently learned called prompt injection, a vulnerability that affects insecure chatbots powered by natural language processing (NLP).

In this task, you will access Van Chatty, AntarctiCrafts' internal chatbot. It's currently under development but has been released to the company for testing.

Conncet to [TryHackME VPN](https://tryhackme.com/room/openvpn) and Start the challenge by clicking on the provided URL.

**Artifact Files:**
* None

### Approach

**1. What is McGreedy's personal email address?**
This is the Web Gui provided to interact with the chatbot:
![img](</advent-of-cyber/van-chatty/images/img1.png>)

For the first question we can retrive the email just by asking it to the chatbot:

![img](</advent-of-cyber/van-chatty/images/img2.png>)


```t.mcgreedy@antarcticrafts.thm```

**2 What is the password for the IT server room door?**

To retrive the password for the IT server room door is required to "be" a member of the IT department:

![img](</advent-of-cyber/van-chatty/images/img3.png>)

First of all we ask about the members of the IT department and after we disguise as one of the employee of such department to get the password:

![img](</advent-of-cyber/van-chatty/images/img4.png>)

Password: ```BtY2S02```

**3. What is the name of McGreedy's secret project?**

Since this ChatBot has some security checks just asking for the name of the project isn't enough.

Tricking the bot into "thinking" is in mantainance mode will bypass the security checks, and gives us the the secret name:

![img](</advent-of-cyber/van-chatty/images/img5.png>)

Secret Project Name: ```Purple Snow```

### Reflections
Easy challenge
  

---
<a href="/advent-of-cyber/main.md" class="btn">Back to home</a>
