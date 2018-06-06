from typing import Callable


def use_cpu(count) -> Callable[[], None]:
    def _use_cpu():
        a = 0
        for x in range(1, count):
            a = a + 1
        return

    return _use_cpu
