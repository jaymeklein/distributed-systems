import Pyro5.api


def connect_to_calculator():
    with Pyro5.api.Proxy("PYRONAME:example.calculator") as calculator:
        return calculator


def main():
    calc = connect_to_calculator()

    print("Adição: 10 + 5 =", calc.add(10, 5))
    print("Subtração: 10 - 5 =", calc.sub(10, 5))
    print("Multiplicação: 10 * 5 =", calc.mult(10, 5))
    print("Divisão: 10 / 5 =", calc.div(10, 5))
    print("Divisão por zero: 10 / 0 =", calc.div(10, 0))


if __name__ == "__main__":
    main()
