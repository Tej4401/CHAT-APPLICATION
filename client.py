import socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.43.26", 4442))
msg = connection.recv(1024).decode()
print(msg)
while(True):
    msg1 = input(">> ").encode()
    connection.send(msg1)
    msg = connection.recv(1024).decode()
    print("<< " + msg)