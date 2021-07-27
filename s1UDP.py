import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Berjaya buat sokett")

port = 8888

s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

while True:
        data, address = s.recvfrom(1024)
        print(data)
        s.sendto(b'Terima kasih!', address)
c.close()

