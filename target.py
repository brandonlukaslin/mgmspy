import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect(('192.168.100.25', 9999))
