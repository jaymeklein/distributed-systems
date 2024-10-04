import socket


def server_program():
    host = "127.0.0.1"
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    print("Servidor esperando por conexões...")

    conn, address = server_socket.accept()
    print(f"Conexão estabelecida de {address}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"Valor recebido do cliente: {data}")

        conn.send("Valor recebido com sucesso".encode())

    conn.close()


if __name__ == "__main__":
    server_program()
