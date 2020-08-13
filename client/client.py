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



# client.py

# Necessary libraries.
import socket
import threading


# Server Data
sv_host = '127.0.0.1'
sv_port = 55555

# Size limit for messages.
buffer_size = 1024

# Let the user choose their nickname.
nick = input("What name would you like to go by?  ")

# Connecting to the server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((sv_host, sv_port))


# Listening on the server and checking for incoming messages.
def receive():
	while True:
		# Try receiving messages from server.
		try:
			msg = client.recv(buffer_size).decode('ascii')
			# Check if msg == 'NICK' and if true send the nickname to the server.
			if msg == 'NICK':
				client.send(nick.encode('ascii'))
			else:
				print(msg)

		except Exception as e:
			# Close connection on error.
			print(f"An error occured: {e}")
			client.close()
			
			break


# Function used to print all the messages onto the user's terminal.
def write():
	while True:
		msg = f"{nick}: {input('')}"
		client.send(msg.encode('ascii'))


# Initializing threads for writing and listening.
rcv_thread = threading.Thread(target=receive)
rcv_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()