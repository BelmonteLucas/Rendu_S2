from scapy.all import ARP, Ether, srp
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
    s.close()
    return IP

local_ip = get_local_ip()
subnet = local_ip.rsplit('.', 1)[0] + '.0/16'

arp = ARP(pdst=subnet)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp

print(f"Scanning {subnet}...\n")
result = srp(packet, timeout=3, verbose=True)[0]

for sent, received in result:
    print(f"IP: {received.psrc} — MAC: {received.hwsrc}")
