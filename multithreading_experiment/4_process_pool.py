import concurrent.futures
from concurrent.futures import Future
from timeit import default_timer as timer
from typing import Callable, List

from multithreading_experiment.cpu_task import class_use_cpu
from multithreading_experiment.download_site import *


class MyProcessPoolExecutor:

    def __init__(self, max_workers=0):
        self.max_workers = max_workers

    def do(self, what: Callable[[], None], count: int):
        futures: List[Future] = []

        with concurrent.futures.ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            for i in range(0, count):
                future = executor.submit(what)
                futures.append(future)

        for future in futures:
            future.result()


if __name__ == "__main__":
    prepare_directory()
    start = timer()
    # MyProcessPoolExecutor(max_workers=4).do(url_get, 20)
    MyProcessPoolExecutor(max_workers=4).do(class_use_cpu(10000000), 20)
    # MyProcessPoolExecutor(max_workers=8).do(cpu_without_gil, 20)
    end = timer()
    print("{}s".format(end - start))
