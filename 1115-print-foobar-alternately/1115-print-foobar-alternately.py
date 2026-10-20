import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_semaphore = threading.Semaphore(1)
        self.bar_semaphore = threading.Semaphore(0)

    def foo(self, printFoo) -> None:
        for i in range(self.n):
            self.foo_semaphore.acquire()
            printFoo()
            self.bar_semaphore.release()

    def bar(self, printBar) -> None:
        for i in range(self.n):
            self.bar_semaphore.acquire()
            printBar()
            self.foo_semaphore.release()