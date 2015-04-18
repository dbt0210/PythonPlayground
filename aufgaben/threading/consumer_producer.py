import time
import threading
import random

# Setup code: initialize Queue, Consumer, Producer
q = []


def produce():
    while running:
        q.append("A task")
        print("Appending task to queue")
        time.sleep(random.randrange(50)/100)


def consume():
    while running:
        if len(q) > 0:
            q.pop()
            print("Removing task from queue")
        time.sleep(random.randrange(70)/100)


t1 = threading.Thread(name="Producer", target=produce)
t2 = threading.Thread(name="Consumer", target=consume)


# Running code:
running = True
t1.start()
t2.start()

time.sleep(20)
running = False

print(len(q))
