import threading
import time

counter1 = 0
counter2 = 0


def thread1():
    global counter1
    while running:
        counter1 += 1
        print("Thread #1: counter =", counter1)
        time.sleep(5)


def thread2():
    global counter2
    while running:
        counter2 += 1
        print("Thread #2: counter =", counter2)
        print("Counter difference =", counter2 - counter1)
        time.sleep(3)


th1 = threading.Thread(target=thread1)
th2 = threading.Thread(target=thread2)
running = True
th1.start()
th2.start()
time.sleep(30)
running = False
