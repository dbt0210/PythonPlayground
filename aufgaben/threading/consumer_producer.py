import time
import threading
import random
import queue

# Setup code: initialize Queue, Consumer, Producer
q = queue.Queue()


def produce():
    while running:
        taskno = random.randint(0, 1000)
        q.put(taskno)
        print("Queueing task", taskno)
        time.sleep(random.randrange(50)/100)


def consume():
    while running:
        if q.qsize() > 0:
            taskno = q.get()
            print("Removing task {} from queue".format(taskno))
        time.sleep(random.randrange(70)/100)


t1 = threading.Thread(name="Producer", target=produce)
t2 = threading.Thread(name="Consumer", target=consume)


# Running code:
running = True
t1.start()
t2.start()

time.sleep(5)
running = False

print(q.qsize())
