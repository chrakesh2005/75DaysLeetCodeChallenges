from threading import Condition

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.condition = Condition()

    def fizz(self, printFizz):
        while True:
            with self.condition:
                while self.i <= self.n and self.i % 3 == 0 and self.i % 5 != 0:
                    printFizz()
                    self.i += 1
                    self.condition.notify_all()
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                self.condition.wait()

    def buzz(self, printBuzz):
        while True:
            with self.condition:
                while self.i <= self.n and self.i % 5 == 0 and self.i % 3 != 0:
                    printBuzz()
                    self.i += 1
                    self.condition.notify_all()
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                self.condition.wait()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.condition:
                while self.i <= self.n and self.i % 15 == 0:
                    printFizzBuzz()
                    self.i += 1
                    self.condition.notify_all()
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                self.condition.wait()

    def number(self, printNumber):
        while True:
            with self.condition:
                while self.i <= self.n and self.i % 3 != 0 and self.i % 5 != 0:
                    printNumber(self.i)
                    self.i += 1
                    self.condition.notify_all()
                if self.i > self.n:
                    self.condition.notify_all()
                    return
                self.condition.wait()