import logging
import random
import time
from queue import PriorityQueue
import threading
class Task(threading.Thread):
    def __init__(self,sem:threading.Semaphore):
        super().__init__()
        self.t = random.uniform(0, 1)
        self.sem = sem
    def run(self):
        with self.sem:
            print(f"Task sleep({self.t})")
            time.sleep(self.t)

    def __lt__(self, obj):
        if not isinstance(obj, Task):
            return NotImplemented
        return self.t < obj.t

    def __gt__(self, obj):
        if not isinstance(obj, Task):
            return NotImplemented
        return self.t > obj.t
class Producer(threading.Thread):
    def __init__(self, sem: threading.Semaphore, task_queue:PriorityQueue):
        super().__init__()
        self.sem = sem
        self.task_queue = task_queue

    def run(self) -> None:
        print("Producer: Running")
        with self.sem:
            for _ in range(10):
                t = random.randint(0,10)
                task = Task(self.sem)
                print(f"Added task in queue with priority {t}")
                time.sleep(random.randint(0,1))
                self.task_queue.put((t,task))
        print("Producer: Done")

class Consumer(threading.Thread):
    def __init__(self, sem: threading.Semaphore, task_queue:PriorityQueue):
        super().__init__()
        self.sem = sem
        self.task_queue = task_queue


    def run(self) -> None:
        self.sem.acquire()
        print("Consumer: Running")
        self.sem.release()
        while not self.task_queue.empty():
            temp = self.task_queue.get()
            print(f"> running priority({temp[0]})")
            temp[1].start()
            temp[1].join()
        print("Consumer: Done")




def main():
    sem = threading.Semaphore()
    task_queue = PriorityQueue()
    pool = []
    prod = Producer(sem,task_queue)
    prod.start()
    pool.append(prod)
    cons = Consumer(sem,task_queue)
    cons.start()
    pool.append(cons)
    for i in pool:
        i.join()






if __name__ == "__main__":
    main()
