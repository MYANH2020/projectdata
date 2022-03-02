#first of all import the socket library
import socket
HOST = '127.0.0.1'
PORT = 8000
#create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#next bind to the port
#input an empty string to make the server listen to requests
#coming from  other computers on the network
server.bind((HOST, PORT))
server.listen(1)
#applied a while loop until it is interrupt or
#when an error occurs
while True:
    # establish connection with client
    conn, client = server.accept()
    try:
        print("Connection from", client)
        while True:
            data = conn.recv(1024)
            print("Message from Client: " + data)
            conn.sendall(data[::-1])
            if data == "end":
             #breaking once connection closed
                break
    finally:
            conn.close()
    
    server.close()


    
