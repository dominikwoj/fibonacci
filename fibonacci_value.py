def fib(y):
    '''
    >>> fib(1)
    0
    >>> fib(2)
    1
    >>> fib(3)
    1
    >>> fib(4)
    2
    >>> fib(5)
    3
    >>> fib(6)
    5
    '''
    x = y - 1

    def fib_in(x):
        return 1 if x in [1, 2] else fib_in(x - 1) + fib_in(x - 2)

    return 0 if x == 0 else fib_in(x)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
