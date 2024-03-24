def isNumPalindrome(x):

    """
    >>> isNumPalindrome(121)
    True
    >>> isNumPalindrome(344)
    False
    >>> isNumPalindrome(-121)
    False
    >>> isNumPalindrome("Hello")
    'Error'
    """
    temp = x
    rev = 0
    if isinstance(x, int):
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x//10
        if (temp == rev):
            return True
        else:
            return False
    else:
        return "Error"