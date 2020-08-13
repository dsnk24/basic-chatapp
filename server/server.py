#    Copyright 2020 Tabacaru Eric
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.



# server.py

# Necessary libraries.
import socket
import threading

# Specifications for the server address and port
host = '127.0.0.1'
port = 55555

# Size limit for messages
buffer_size = 1024

# Server Initialization
sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv.bind((host, port))
sv.listen()

# client and nickname list
clients = []
nicks = []


# Function used to send a message from the server to all the other connected clients
def broadcast_msg(msg):
	for c in clients:
		c.send(msg)


def handle(client):
	while True:
		try:
			# Try broadcasting messages limited by the buffer size.
			msg = client.recv(buffer_size)
			broadcast_msg(msg)

		except:
			# If an error occurs, remove the client and close them.
			idx = clients.index(client)
			clients.remove(client)
			client.close()

			nick = nicks[idx]
			
			broadcast_msg(f"{nick} has left!".encode('ascii'))

			nicks.remove(nick)

			break

def receive():
	while True:
		# Accept a new connection.
		client, addr = sv.accept()
		print(f"Connected with {addr}")


		# Request and store the nickname.
		client.send('NICK'.encode('ascii'))
		nick = client.recv(buffer_size).decode('ascii')
		nicks.append(nick)
		clients.append(client)


		# Broadcast the nickname and tell the other clients that a new connection was made.
		print(f"Nickname is {nick}")
		broadcast_msg(f"{nick} has joined the chat!".encode('ascii'))
		client.send("Connected to server!".encode('ascii'))


		# Initialize and handle thread for the client.
		thread = threading.Thread(target=handle, args=(client,))
		thread.start()


# Start Server.
receive()