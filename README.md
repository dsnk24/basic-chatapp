# Chat Application made in Python

This is a chat application I made in Python using the Socket and Threading built-in libraries.

To successfully run this program, you have to first run the `server.py` file to initialize the server and then open another terminal and run the `client.py` file to initialize and connect to the server. You can connect as many clients as you like but I recommend keeping it at a maximum of 20.

*DISCLAIMER:*
This is designed to run on your local machine using the loop-back IP address (`127.0.0.1`). It can be modified to work on a server but you will need to modify the server data variables and make a worker that automatically runs the `server.py` file on the dedicated server.