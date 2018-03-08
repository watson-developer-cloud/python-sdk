import warnings

def deprecated(message):
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn(
                "{} is a deprecated function. {}".format(
                    func.__name__, message),
                category=DeprecationWarning,
                stacklevel=2)
            return func(*args, **kwargs)

        return deprecated_func

    return deprecated_decorator
