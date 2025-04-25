# Imports should be at the top
import threading
from threading import Thread
import time


def temp1():
    for x in range(1):
        print("processo1", x)
        x = 1


# First example
def example1():
    # Create and start the thread
    t1 = Thread(target=temp1)
    t1.start()

    # Thread information examples
    print(f"Active thread count: {threading.active_count()}")
    print(f"Current thread: {threading.current_thread().name}")
    print(f"All active threads: {threading.enumerate()}")


# Second example
def proc1():
    for x in range(1, 11):
        print("processo 1", x)
        time.sleep(1)


def proc2():
    for x in range(1, 11):
        print("processo 2", x)
        time.sleep(2)


def example2():
    # Create and start both threads
    t1 = Thread(target=proc1)
    t2 = Thread(target=proc2)

    t1.start()
    t2.start()

    # Print thread information
    print(f"Active thread count: {threading.active_count()}")
