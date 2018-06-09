import hashlib


def cpu_without_gil():
    """As documented: https://docs.python.org/3/library/hashlib.html#hash-algorithms, hashing releases GIL"""
    count = 10000
    m = hashlib.sha256()
    m.update(b"Nobody inspects" * count)
    m.update(b" the spammish repetition" * count)
    m.digest()
