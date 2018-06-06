from timeit import default_timer as timer

from multithreading_experiment.download_site import url_get, clear_directory


def single_download(count: int):
    for i in range(0, count):
        url_get()


if __name__ == "__main__":
    clear_directory()

    start = timer()
    single_download(5)
    end = timer()
    print(end - start)
