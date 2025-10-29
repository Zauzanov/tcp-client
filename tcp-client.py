import socket

target_host = "127.0.0.1"
target_port = 9998

# create socket object - IPv4/TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to the server
client.connect((target_host, target_port))

# send some data in the form of bytes
client.send(b"GET / HTTP/1.1\r\nHost: 192.168.204.129\r\n\r\n")

# receive some data
response = client.recv(4096)


print(response.decode())
client.close()                                  # close the socket
