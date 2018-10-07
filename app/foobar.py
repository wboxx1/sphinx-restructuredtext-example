# -*- coding: utf-8 -*-

def hello_world():
    """function that returns Hello World!

    :returns: Hello World!
    :rtype: string
    :Example:

    >>> import foobar
    >>> foobar.hello_world()
    Hello World!
    """
    return("Hello World!")

def reverse(input_string):
    """function that reverses input string

    :param input_string: String to reverse
    :type input_string: string
    :returns: reverse of input_string
    :rtype: string
    :Example:

    >>> import foobar
    >>> foobar.reverse("Hello World!")
    !dlroW olleH
    """
    return(input_string[::-1])