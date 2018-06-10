from typing import Callable


class class_use_cpu(object):
    def __init__(self, count):
        self.count = count

    def __call__(self):
        a = 0
        for x in range(1, self.count):
            a = a + 1
        return


def use_cpu(count) -> Callable[[], None]:
    def _use_cpu():
        a = 0
        for x in range(1, count):
            a = a + 1
        return

    return _use_cpu
