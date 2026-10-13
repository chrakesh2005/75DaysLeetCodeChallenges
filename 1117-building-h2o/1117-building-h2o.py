from threading import Semaphore

class H2O:
    def __init__(self):
        self.hydrogen_sem = Semaphore(2)
        self.oxygen_sem = Semaphore(0)
        self.lock = Semaphore(1)
        self.h_count = 0

    def hydrogen(self, releaseHydrogen):
        self.hydrogen_sem.acquire()
        releaseHydrogen()
        self.lock.acquire()
        self.h_count += 1
        if self.h_count == 2:
            self.h_count = 0
            self.oxygen_sem.release()
        self.lock.release()

    def oxygen(self, releaseOxygen):
        self.oxygen_sem.acquire()
        releaseOxygen()
        self.hydrogen_sem.release()
        self.hydrogen_sem.release()