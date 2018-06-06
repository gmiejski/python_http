from queue import Queue, Empty
from threading import Thread
from timeit import default_timer as timer
from typing import Callable

from multithreading_experiment.cpu_task import use_cpu
from multithreading_experiment.download_site import url_get, prepare_directory


def worker(queue: Queue, ):
    def _worker():
        while True:
            try:
                func = queue.get_nowait()
                func()
                queue.task_done()
            except Empty:
                break

    return _worker


class QueueBasedExecutor:

    def __init__(self, max_threads=0):
        self.max_threads = max_threads

    def do(self, what: Callable[[], None], count: int):
        queue = Queue(count)
        threads_total = self.max_threads if self.max_threads != 0 else count

        for i in range(0, count):
            queue.put(what)

        threads = []
        for i in range(0, threads_total):
            thread = Thread(target=worker(queue))
            thread.start()
            threads.append(thread)

        queue.join()

        for t in threads:
            t.join()


if __name__ == "__main__":
    prepare_directory()
    start = timer()
    QueueBasedExecutor(max_threads=0).do(url_get, 20)
    QueueBasedExecutor(max_threads=0).do(use_cpu(1000000), 20)
    end = timer()
    print(end - start)
