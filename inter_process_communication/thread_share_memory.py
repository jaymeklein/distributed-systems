import threading
import time
import queue

q = queue.Queue()


def producer():
    count = 0
    while True:
        q.put(count)
        count += 1
        time.sleep(1)


def consumer():
    while True:
        value = q.get()
        print(f"Valor consumido: {value}")
        time.sleep(1)


if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
