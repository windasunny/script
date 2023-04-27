import socket
import threading

# 測試服務、發送垃圾數據、進行Fuzz

IP = '127.0.0.1'
PORT = 8080

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))

    # 最大連接數 5
    server.listen(5)
    print(f'[*] Listen on {IP}:{PORT}')

    try:
        while True:
            # 客戶端成功建立連接
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]:{address[1]}}')
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
    except KeyboardInterrupt:
        print("[*] Closing server...")
        server.close()
        print("[*] Server closed")

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()

