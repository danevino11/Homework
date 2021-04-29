In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'


def cache_func(times: int):
    cache_dict_2 = {}

    def wrapper(func):
        def inside(*args):
            if args not in cache_dict_2:
                val = func(*args)
                cache_dict_2[args] = [val, 0]
                return cache_dict_2[args][0]
            elif cache_dict_2[args][1] < times:
                cache_dict_2[args][1] += 1
                return cache_dict_2[args][0]
            else:
                val = func(*args)
                cache_dict_2[args] = [val, 0]
                return val

        return inside

    return wrapper