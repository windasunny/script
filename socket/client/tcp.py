import socket

host = "127.0.0.1"
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.send(b"Hello world")
response = client.recv(4096)

print(response.decode())
client.close()
