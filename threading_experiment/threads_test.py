from threading import Thread


class AnotherThread(Thread):

    def run(self) -> None:
        print("Thread job started")
        a = 0
        for x in range(1, 100000000):
            a = a + 1
        print("Thread job finished: " + str(a))


def thread_start() -> Thread:
    thread = AnotherThread()
    thread.start()
    return thread


if __name__ == "__main__":
    thr1 = thread_start()
    thr2 = thread_start()
    thr3 = thread_start()
    thr4 = thread_start()
    thr5 = thread_start()
    thr6 = thread_start()
    thr7 = thread_start()
    thr8 = thread_start()
    thr1.join()
    print("Done")
