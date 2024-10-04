import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("Adição: 5 + 3 =", proxy.add(5, 3))
print("Subtração: 10 - 4 =", proxy.subtract(10, 4))
print("Multiplicação: 6 * 7 =", proxy.multiply(6, 7))
print("Divisão: 20 / 5 =", proxy.divide(20, 5))
print("Divisão por zero: 10 / 0 =", proxy.divide(10, 0))
