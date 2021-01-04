import socket

HOST = 'localhost'
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
client, address= server.accept()

while True:
	print('Server listen.....')
	inp = input(f"Connected To {address} Masukan Perintah : ")
	client.send(inp.encode('utf-8'))
	print(client.recv(1024).decode('utf-8'))
