import threading
import time

zaehler1 = 0
zaehler2 = 0

def Thread1():
    global zaehler1
    while 1:
        time.sleep(5)
        zaehler1 = zaehler1 + 1
        print("Thread 1: zaehler=", zaehler1)

def Thread2():
    global zaehler1, zaehler2
    while 1:
        time.sleep(3)
        zaehler2 = zaehler2 + 1
        print("Thread 2: zaehler=", zaehler2)
        print("Differenz der beiden Zaehler=", zaehler2 - zaehler1)

th1 = threading.Thread(target=Thread1)
th2 = threading.Thread(target=Thread2)
th1.start()
th2.start()
