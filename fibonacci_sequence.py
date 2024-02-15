def fib_numbers(x):
    '''
    >>> fib_numbers(0) is None
    True
    >>> fib_numbers(1)
    [0]
    >>> fib_numbers(2)
    [0, 1]
    >>> fib_numbers(3)
    [0, 1, 1]
    >>> fib_numbers(4)
    [0, 1, 1, 2]
    >>> fib_numbers(5)
    [0, 1, 1, 2, 3]
    >>> fib_numbers(6)
    [0, 1, 1, 2, 3, 5]
    >>> fib_numbers(7)
    [0, 1, 1, 2, 3, 5, 8]
    >>> fib_numbers(8)
    [0, 1, 1, 2, 3, 5, 8, 13]
    >>> fib_numbers(9)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    '''

    l = [0, 1]
    # if x == 0:
    #     return None
    # if x == 1:
    #     return [0]
    # elif x == 2:
    #     return l

    match x:
        case 0:
            return None
        case 1:
            return [0]
        case 2:
            return l

    def fib_list(x, l):
        l.append(l[-1] + l[-2])
        return l if x == len(l) else fib_list(x, l)

    return fib_list(x, l)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
