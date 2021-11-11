def is_leximin_better(x: list, y: list) -> bool:
    # return true iff x is leximin-better than y.

    """
    :param x: list, y: list
    :return bool

    >>> [is_leximin_better([3, 1, 3], [2, 99, 1])]
    [True]

    >>> [is_leximin_better([2, 99, 1], [3, 1, 3])]
    [False]

    >>> [is_leximin_better([50, 100], [50, 50])]
    [True]

    >>> [is_leximin_better([0, 4, 3, 2], [4, 3, 0, 2])]
    [False]

    >>> [is_leximin_better([1.5, 2.4, 7.9, 3.601, 3.59, 2.41], [1.5, 2.4, 7.9, 3.6, 3.59, 2.41])]
    [True]

    >>> [is_leximin_better([14, 13, 12, 11, 11], [10, 11, 12, 13, 14])]
    [True]

    >>> [is_leximin_better([10, 11, 12, 13, 14], [15, 14, 13, 12, 10])]
    [False]

    >>> [is_leximin_better([10, 11, 12, 14, 14], [10, 11, 12, 13, 14])]
    [True]

    >>> [is_leximin_better([0], [1])]
    [False]

    >>> [is_leximin_better([1], [0])]
    [True]
    """

    x.sort()
    y.sort()
    for i, j in zip(x, y):
        if i != j:
            return i > j
    return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()