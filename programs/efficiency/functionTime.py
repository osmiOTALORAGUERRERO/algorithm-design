import time

def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper(*args, **kwargs):
        # Start counting.
        start_time = time.time()
        # Take the original function's return value.
        ret = f(*args, **kwargs)
        # Calculate the elapsed time.
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: %0.10f seconds of function {f.__name__}()." % elapsed_time)
        return ret

    return wrapper
