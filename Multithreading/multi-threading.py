from threading import Thread
import time


class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            time.sleep(1)  # Adding a small delay to make it more apparent in the output.


class Hi(Thread):
    def run(self):
        for i in range(50):
            print('Hi')
            time.sleep(1)  # Adding a small delay to make it more apparent in the output


t1 = Hello()
t2 = Hi()

t1.start()
time.sleep(0.2)
t2.start()

t1.join()


print('Program is finished')
