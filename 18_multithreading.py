# functions
# activeCount(), currentThread(), enumerate(), isDaemon(), is Alive()

# Thread Class Methods
# run(), start(), join()

from threading import *
import threading
from time import sleep

class example(Thread):
    def run(self):
        for i in range(5):
            print("thread 1")
            sleep(1)

class example2(Thread):
    def run(self):
        for i in range(5):
            print("thread 2")
            sleep(1)

ex = example()
ex2 = example2()
ex.start()
sleep(0.1)
ex2.start()
ex.join()
ex2.join()

print("END of the program")

#################
# lock methods
# acquire() - lock
# release() - unlock

lock = threading.Lock()
class lockExample(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print("Lock acquired 1")
            sleep(1)
            lock.release()

class lockExample2(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print("Lock acquired 2")
            sleep(1)
            lock.release()

lex = lockExample()
lex2 = lockExample2()
lex.start()
sleep(0.1)
lex2.start()