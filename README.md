# projectdata
Objectives
The purpose of this lab is to learn how to write a server and client socket program. The TCP socket program description is the following exercise. 
You can work alone or a group of two students.
Exercise (100 points)
Reverse-echo-serve and client: in this programming assignment, you are going to build a simple reverse echo server and a client using TCP socket. The server and client should run at different machines.
 
1) Reverse echo server
A reverse echo server receives a message from a client over TCP socket and replies the same message back to the source in reverse order. For example, if a sever gets a message “GOOD” from a client, then the reverse echo server sends back the message “DOOG” to the client.
The server program should be terminated if it gets “end” message from a client after it replies “dne” message to the client. Note that please use port number over 5000.
A reverse echo server begins by a user at any machines by a command line:

2) Echo Client
An echo client gets a message from a user and sends the message to the connected reverse echo server. When the reversed message is arrived from the server, it displays the message to the users.
If a user wants to stop the client program, the user types “end” to the client. The client sends the message to the reverse echo server, and waits the message “dne” from the server. If the client gets the message “dne”, it terminates itself with displaying “dne” message.
The echo client is started by the following command line:
![image](https://user-images.githubusercontent.com/63695763/156285992-effef41f-3bbf-42e1-95e2-254247bf968a.png)
command to run:
use python 2.xxx
command: python server.py
python client.py 
Message from Client: good
Response from Server: doog
Message from Client: hello
Response from Server: olleh
Message from Client: end
Response from Server: dne

