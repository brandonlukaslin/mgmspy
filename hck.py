import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('192.168.100.25', 9999))
print('Menunggu Koneksi ...')
soc.listen(1)

koneksi = soc.accept()
_target = koneksi[0]
ip = koneksi[1]
print(_target)
print(f'Terhubung ke {str(ip)}')