This is a compilation of CSC344 Assignments & Labs.

// Assignment 1: Error Detection

Wrote the computeCheckSum() and verifyCheckSum() methods.

Instructions TLDR:
Implement error detection using a single parity bit for every 7 bits. Modify the most-significant bit
to have the parity we choose. This turns the ASCII character into a Unicode character. If there is a one-bit 
error (in other words, flip any single bit), then the parity will not match and we can know that the character 
that we received is incorrect.

// Assignment 2: Error Correction 

Wrote the encodeMessage() and correctMessage() methods.

Instructions TLDR:
You will convert the 7 bits of the ASCII code for a character into 11 bits with bits 1, 2, 4, and 8 as the checkbits 
according to the Hamming Codes algorithm. You will also need to be able to correct 1-bit errors by determining, based 
upon which checkbits do not have the correct parity, which bit was in error and fixing it.

// Asssignment 3: IP Forwarding

Instructions TLDR:
Write a program to implement a forwarding algorithm based upon IPv4 addresses. Your program should take as input (user 
input or on the command line) that is an IP address in standard form.  Your program should have a routing table based 
upon the data below, determine the outgoing port number to forward the "so called" packet, and report that port number. 
Routing table was based on a provided image of 4 routers + 4 local machines + 1 port to the Internet with IP addresses 
and prefixes.

