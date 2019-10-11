import socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
listener.bind(("192.168.43.26",4442))
listener.listen(5)
print("[+] waiting for incoming connections")
c,a = listener.accept()
print("[+] connection established")
msg = "[+] connection established"
c.send(msg.encode())
while(True):
    msg = c.recv(1024).decode()
    print("<< " + msg)
    msg1 = input(">> ").encode()
    c.send(msg1)