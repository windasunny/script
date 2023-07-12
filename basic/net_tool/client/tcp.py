import socket


def send(host, port, data):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        client.send(str.encode(data))
        response = client.recv(4096)

        print(response.decode())
        client.close()
    except socket.error as e:
        print("[-] Failed to connect: " + str(e))
