import threading


# Threading allows us to speed up programs by executing multiple tasks at the same time
# Each task will run on it's own thread
# Each thread can run simultaneously and share the data with each other

# Every thread when you start it must do something, which we can define with a function
# our threads will then target these functions
# When we start the threads, the target functions will be run.

def Function1():
    for x in range(10):
        print("ONE")


def Function2():
    for x in range(10):
        print("TWO")


def Function3():
    for x in range(10):
        print("THREE")


# If we call these functions, we see the first function call Must be complete before the next
# They are executed linearly
"""
Function1()
Function2()
Function3()
"""

# We can execute these functions concurrently using threads. We must have a target for a thread
t1 = threading.Thread(target=Function1)
t2 = threading.Thread(target=Function2)
t3 = threading.Thread(target=Function3)

t1.start()
t2.start()
t3.start()

# threads can only run once. If you want to reuse, you must redefine.
t1 = threading.Thread(target=Function1)
t1.start()
# if you want to pause the main program until a thread is done you can!
t1 = threading.Thread(target=Function1)
t1.start()
t1.join() # this will pause the program until the thread is complete
print("Threading rules!")
