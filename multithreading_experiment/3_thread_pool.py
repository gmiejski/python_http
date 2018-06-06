from concurrent.futures import ThreadPoolExecutor, Future
from timeit import default_timer as timer
from typing import List

from multithreading_experiment.download_site import url_get


def thread_pool_download(count: int, max_threads=None):
    futures: List[Future] = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i in range(0, count):
            future = executor.submit(url_get)
            futures.append(future)

        for future in futures:
            future.result()


if __name__ == "__main__":
    start = timer()
    thread_pool_download(20, max_threads=None)
    end = timer()
    print(end - start)
