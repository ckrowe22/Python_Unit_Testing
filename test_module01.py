from module01 import Circle


def circle_test():
    """
    >>> c1 = Circle(2.5)
    >>> c1.radius
    2.5
    >>> c1.area()
    19.63
    >>> c1.circumference()
    15.71
    >>> c1.volume()
    65.45
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
