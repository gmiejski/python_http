from concurrent.futures import ThreadPoolExecutor, Future
from timeit import default_timer as timer
from typing import List, Callable

from multithreading_experiment.cpu_task import use_cpu
from multithreading_experiment.download_site import url_get, prepare_directory


class MyThreadPoolExecutor:

    def __init__(self, max_threads=0):
        self.max_threads = max_threads

    def do(self, what: Callable[[], None], count: int):
        futures: List[Future] = []
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for i in range(0, count):
                future = executor.submit(what)
                futures.append(future)

            for future in futures:
                future.result()


if __name__ == "__main__":
    prepare_directory()
    start = timer()
    MyThreadPoolExecutor(max_threads=1).do(url_get, 20)
    MyThreadPoolExecutor(max_threads=1).do(use_cpu(1000000), 20)
    end = timer()
    print(end - start)
