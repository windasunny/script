import socket
import threading
import time


#  test server, send data, and fuzz


# create a tcp fuzz
def fuzz(host, port):
    return


# create a socket tcp proxy
def proxy(host, port):
    return


def connect(host, port):
    try:
        boolean = True
        while boolean:
            time.sleep(1)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.settimeout(2)
            response = server.connect_ex((host, port))
            if response == 0:
                print(f"[*] Connect success to {host}:{port}")
            else:
                print(f"[-] Connect failed to {host}:{port}")
    except KeyboardInterrupt:
        print("[-] Closing server...")
        server.close()
        print("[-] Server closed")
        boolean = False


def listen(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((host, port))

        server.listen(5)
        print(f"[*] Listen on {host}:{port}")

        while True:
            client, address = server.accept()
            print(f"[*] Accepted connection from {address[0]:{address[1]}}")
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()

    except KeyboardInterrupt:
        print("[-] Closing server...")
        server.close()
        print("[-] Server closed")

    except socket.error as e:
        print("[-] Failed to bind: " + str(e))


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b"ACK")


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 1234
    listen(host, port)
