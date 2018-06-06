from queue import Queue, Empty
from threading import Thread
from timeit import default_timer as timer

from multithreading_experiment.download_site import url_get


def worker(queue: Queue):
    def _worker():
        while True:
            try:
                queue.get_nowait()
                url_get()
                queue.task_done()
            except Empty:
                break

    return _worker


def queued_download_all_threads(count: int, max_threads=0):
    queue = Queue(count)

    threads_total = max_threads if max_threads != 0 else count

    for i in range(0, count):
        queue.put(1)

    threads = []
    for i in range(0, threads_total):
        thread = Thread(target=worker(queue))
        thread.start()
        threads.append(thread)

    queue.join()

    for t in threads:
        t.join()


if __name__ == "__main__":
    start = timer()
    queued_download_all_threads(20, max_threads=0)
    end = timer()
    print(end - start)
