# ICMP-SENDER
Build ICMP-SENDER
1.what is ICMP:
ICMP (Internet Control Message Protocol) is a core protocol in the Internet Protocol Suite, primarily used for network diagnostics and error reporting  and works closely with the Internet Protocol (IP).
 ICMP message type:
echo reply ----> Response to a ping (Echo request)
Echo request ----> sent by ping check 
Time exceeded ---> TTL(TIME-TO-LIVE) EXCEEDED; USED BY TRACEROUTE
Destination unreachable -----> Indicates the destination host or network is unreachable

2.HOW TO SEE PAQUETS ICMP IN WIRESHARK:
First need to VM(VIRTUAL MACHINE)
AFTER THAT IF U HAVE WIRESHARK IN URE APPLICATION FINE 
IF DONT HAVE RUN THESE COMMAND:
     Ubuntu/Debian-based systems:
    open terminal:
    sudo apt update
    sudo apt install wireshark
to verifier installation:
wireshark --version

lunch wireshark: in terminal ---> sudo wireshark
First choose the interface the VM is connected to know that back to terminal tap
ifconig : than can see interface u most see like that (eth0)
back to wireshark and choose interface 2 click to start receive packet 
put in the of filter icmp to filter the packet because whe have a lot of protocole can receive
to see packet back terminal and put:
ping google.com can see know the packet
can see the request and reply from the destination(google.com but is give the ip address because DNS resolute the ip address of namespace)

3.WHAT IS ICMP NETWORK LAYER -- IMAGES
4.what is Scapy? WHy ween need it ??
is a powerful Python-based interactive packet manipulation program and library.
It allows users to create and modify send  and analyze network packets. 

we need to : Packet crafting and manipulation and  Network scanning and Protocole analysis and Traffic Generation and security testing
![Example Image](image/L1.png)
![Example Image](image/L2.png)  


 
use the code and test in your kali 
first lunch python code 
and lunch wireshark
and we says the packet is sender and receive with the configuration the packet
![Example Image](image/L3.png)  

