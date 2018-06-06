from timeit import default_timer as timer
from typing import Callable

from multithreading_experiment.cpu_task import use_cpu
from multithreading_experiment.download_site import url_get, prepare_directory


class SingleThreadExecutor:

    def do(self, what: Callable[[], None], count: int):
        for i in range(0, count):
            what()


def single_download(count: int):
    for i in range(0, count):
        url_get()


if __name__ == "__main__":
    prepare_directory()

    start = timer()
    SingleThreadExecutor().do(use_cpu(1000000), 5)
    SingleThreadExecutor().do(url_get, 5)
    end = timer()
    print(end - start)
