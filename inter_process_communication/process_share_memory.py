import multiprocessing
import time


def increment_value(shared_value):
    for _ in range(5):
        with shared_value.get_lock():
            shared_value.value += 1
            print(f"Processo A incrementou o valor para: {shared_value.value}")
        time.sleep(1)


def print_value(shared_value):
    for _ in range(5):
        with shared_value.get_lock():
            print(f"Processo B leu o valor: {shared_value.value}")
        time.sleep(1)


if __name__ == "__main__":
    shared_value = multiprocessing.Value("i", 0)

    process_a = multiprocessing.Process(target=increment_value, args=(shared_value,))
    process_b = multiprocessing.Process(target=print_value, args=(shared_value,))

    process_a.start()
    process_b.start()

    process_a.join()
    process_b.join()

    print("Finalizou a execução dos processos.")
