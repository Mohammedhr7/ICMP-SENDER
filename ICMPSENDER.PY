from scapy.all import IP, ICMP, sr1

while True:
    try:
        src_ip = input("Source Ip >>")
        dst_ip = input("Destination Name >>")
        ip_head = IP(src=src_ip, dst=dst_ip)
        # print(ip_head.show())

        icmp_head = ICMP(id=100)

        full_packet = ip_head / icmp_head

        packet_sender = sr1(full_packet)
        if packet_sender:
            print(packet_sender.show())
        user_answer = input("continue??")
        if user_answer.lower() == "y" or user_answer.lower() == "yes":
            continue
        else:
            print("U LEFT")
            break
    except Exception as e:
        print("Please put correctly")
        continue