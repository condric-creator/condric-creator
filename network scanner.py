import socket
host=socket.gethostname()
ip_add_of_host=socket.gethostbyname(host)
print(f"ip address:{ip_add_of_host}")
print(f"host:{host}")