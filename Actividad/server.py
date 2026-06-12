import socket

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(1)

print("Esperando conexión...")

client_socket, address = server.accept()

print(f"Conectado con {address}")

while True:

    # RECIBIR
    mensaje = client_socket.recv(1024).decode('utf-8')

    if mensaje.lower() == "salir":
        print("Cliente desconectado")
        break

    print(f"Cliente: {mensaje}")

    # ENVIAR
    respuesta = input("Vos: ")

    client_socket.send(respuesta.encode('utf-8'))

    if respuesta.lower() == "salir":
        break

client_socket.close()
server.close()