import socket


HOST = '192.168.15.4'
PORT = 7000

def client_socket():
    connected = True
    while connected:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        #if len(client.recv(1024)) != 0:
        #    data = client.recv(1024).decode('utf-8')
        #print(len(client.recv))           
        text = 'Send a message: '
        msg = str(text).encode('utf-8')
        client.sendall(msg)
        data = client.recv(1024).decode('utf-8')
        print(f'Received, {data}')
        break

client_socket()