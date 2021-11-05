from time import sleep
class Hello:
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class Hi:
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.run()
t2.run()

