__import__("os").system("pip install scapy --target=. -qq")

import time
from scapy.all import conf, get_if_addr, get_if_hwaddr, srp, Ether, ARP

def get_network_settings():
    try:
        # Get default interface information
        iface = conf.iface
        ip_address = get_if_addr(iface)
        mac_address = get_if_hwaddr(iface)

        print(f"Interface: {iface}")
        print(f"IP Address: {ip_address}")
        print(f"MAC Address: {mac_address}")

        # ARP scan to discover local devices (timeout 10 seconds)
        print("Scanning the network for devices...")
        start_time = time.time()
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=f"{ip_address}/24")
        answered, _ = srp(arp_request, timeout=10, verbose=0)
        print("Devices found:")
        for sent, received in answered:
            print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

        elapsed_time = time.time() - start_time
        print(f"Scanning completed in {elapsed_time:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_network_settings()
