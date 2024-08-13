import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    while True:
        message = input("Enter message to send: ")
        s.sendall(message.encode())

        data = s.recv(1024)
        print(f"Received from server: {data.decode()}")

        if message.lower() == 'exit':
            break
