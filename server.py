import socket
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 7000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def thread_server(clt, add):
    print(f'New Connection:--> {add} connected.')
    connected = True
    while connected:
        data = clt.recv(1024)
        msg = data.decode('utf-8')
        print(msg)
        if not data: break
        clt.sendall(data)
    #server.shutdown()
    #server.close()
            

def server_connection():
    server.bind((HOST, PORT))
    server.listen(2)
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=thread_server, args=(client, address))
        thread.start()
        thread.join()
        print(f'Clientsocket:--> {threading.activeCount()-1}')
        #thread.join()
        

if __name__ == "__main__":
    server_connection()