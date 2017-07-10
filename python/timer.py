import time

def custom_timer(func):
    """ Return a wrapper to time and execute function `func`
    """
    def wrapper(*args, **kwargs):
        t0 = time.time()
        val = func(*args, **kwargs)
        print('{} took {:.1f} seconds'.format(func.__name__, time.time() - t0))
        return val
    return wrapper
