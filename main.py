from typing import Iterable, Iterator
import doctest


def take(iterable: Iterable, n: int) -> Iterable:
    res = []
    for _ in range(n):
        try:
            res.append(next(iterable))
        except StopIteration:
            break
    return res


def cycle(iterable: Iterable) -> Iterator:
    elems = []
    for i in iterable:
        elems.append(i)
        yield i
    i = 0
    l = len(elems)
    while True:
        yield elems[i]
        i = (i + 1) % l


def chain(*iterables: Iterable) -> Iterator:
    for j in iterables:
        for k in j:
            yield k


def main():
    """
    >>> take(cycle([1, 2, 3]), 10)
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    >>> list(chain([1, 2, 3], ['a', 'b']))
    [1, 2, 3, 'a', 'b']
    >>> take(cycle(chain([True, False], [1, 0])), 9)
    [True, False, 1, 0, True, False, 1, 0, True]

    """


if __name__ == "__main__":
    pass

