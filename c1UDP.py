import socket
import sys

ip = '192.168.56.102'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
       s.sendto(b'Hi, saya client. Terima Kasih!', (ip, port))
       data, address = s.recvfrom(1024)
       print(data)
       sys.exit()

s.close()
