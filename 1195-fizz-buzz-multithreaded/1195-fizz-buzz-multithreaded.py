import threading

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.condition = threading.Condition()

    def fizz(self, printFizz) -> None:
        while True:
            with self.condition:
                while self.current <= self.n and self.current % 3 == 0 and self.current % 5 != 0:
                    printFizz()
                    self.current += 1
                    self.condition.notify_all()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                self.condition.wait()

    def buzz(self, printBuzz) -> None:
        while True:
            with self.condition:
                while self.current <= self.n and self.current % 5 == 0 and self.current % 3 != 0:
                    printBuzz()
                    self.current += 1
                    self.condition.notify_all()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                self.condition.wait()

    def fizzbuzz(self, printFizzBuzz) -> None:
        while True:
            with self.condition:
                while self.current <= self.n and self.current % 15 == 0:
                    printFizzBuzz()
                    self.current += 1
                    self.condition.notify_all()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                self.condition.wait()

    def number(self, printNumber) -> None:
        while True:
            with self.condition:
                while self.current <= self.n and self.current % 3 != 0 and self.current % 5 != 0:
                    printNumber(self.current)
                    self.current += 1
                    self.condition.notify_all()

                if self.current > self.n:
                    self.condition.notify_all()
                    return

                self.condition.wait()