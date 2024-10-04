import socket


def client_program():
    host = "127.0.0.1"
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Digite um número para enviar ao servidor: ")

    while message.lower().strip() != "sair":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Resposta do servidor: {data}")
        message = input("Digite outro número ou 'sair' para finalizar: ")

    client_socket.close()


if __name__ == "__main__":
    client_program()
