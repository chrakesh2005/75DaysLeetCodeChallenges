import threading

class H2O:
    def __init__(self):
        self.h_sem = threading.Semaphore(2)
        self.o_sem = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen) -> None:
        self.h_sem.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.barrier.wait()

    def oxygen(self, releaseOxygen) -> None:
        self.o_sem.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.barrier.wait()
        self.h_sem.release()
        self.h_sem.release()
        self.o_sem.release()