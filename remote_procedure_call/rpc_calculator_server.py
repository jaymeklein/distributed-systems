from xmlrpc.server import SimpleXMLRPCServer
import threading


def add(x: int | float, y: int | float) -> int | float:
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    return x - y


def multiply(x: int | float, y: int | float) -> int | float:
    return x * y


def divide(x: int | float, y: int | float) -> int | float:
    if y == 0:
        return float("inf")

    return x / y


def run_server():
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Servidor RPC rodando na porta 8000...")

    server.register_function(add, "add")
    server.register_function(subtract, "subtract")
    server.register_function(multiply, "multiply")
    server.register_function(divide, "divide")

    server.serve_forever()


server_thread = threading.Thread(target=run_server)
server_thread.start()
