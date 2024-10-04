import Pyro5.api


@Pyro5.api.expose
class Calculator:
    def add(self, num1: int | float, num2: int | float) -> int | float:
        return num1 + num2

    def sub(self, num1: int | float, num2: int | float) -> int | float:
        return num1 - num2

    def mult(self, num1: int | float, num2: int | float) -> int | float:
        return num1 * num2

    def div(self, num1: int | float, num2: int | float) -> int | float:
        if num2 == 0:
            return float("inf")

        return num1 / num2


def start_server():
    with Pyro5.server.Daemon() as daemon:
        with Pyro5.api.locate_ns() as ns:
            uri = daemon.register(Calculator)
            ns.register("example.calculator", uri)
            print("Servidor ativo. Objeto registrado como 'example.calculator'.")
            daemon.requestLoop()


if __name__ == "__main__":
    # python -m Pyro5.nameserver
    start_server()
