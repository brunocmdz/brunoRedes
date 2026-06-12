import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

while True:

    # ENVIAR
    mensaje = input("Vos: ")

    client.send(mensaje.encode('utf-8'))

    if mensaje.lower() == "salir":
        break

    # RECIBIR
    respuesta = client.recv(1024).decode('utf-8')

    if respuesta.lower() == "salir":
        print("Servidor desconectado")
        break

    print(f"Servidor: {respuesta}")

client.close()