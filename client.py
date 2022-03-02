#import socket module
import socket
HOST = '127.0.0.1'
#define the port inwhich we want to connect
PORT = 8000
#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server on local computer
client.connect((HOST, PORT))
# receive data from the server and decoding to get the string.
try:
	while True:
		msg = raw_input("Message from Client: ") #python 2.x version
		#if python 3.x version msg = input("Message from Client: ")
		client.sendall(msg)
		data = client.recv(1024)
		print('Response from Server: ' + data)
		if msg == "end":
			break
finally:
    client.close()