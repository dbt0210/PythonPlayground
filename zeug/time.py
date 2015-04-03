from time import time
from random import random

elements = 10000000

t0 = time()
l = [int(random()*1000) for i in range(0, elements)]
t1 = time()
delta = t1-t0
print("Done creating list. Time: " + str(delta*1000) + "ms. That's " + str(delta*1000/elements) + "ms/Element!")

t0 = time()
l.sort()
t1 = time()
delta = t1-t0
print("Done sorting list. Time: " + str(delta*1000) + "ms. That's " + str(delta*1000/elements) + "ms/Element!")