from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]

"""A python decorator to time functions.                                                                                                 
It outputs the time in a string format using the convention HH:MM:SS.                                                                    
"""

import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)

        time_stop = time.time()
        m, s = divmod(time_stop - time_start, 60)
        h, m = divmod(m, 60)
        run_time = f"{int(h):02d}:{int(m):02d}:{int(s):02d}"

        return result, run_time

    return wrapper

if __name__ == "__main__":

    @time_it
    def example_func(n):
        time.sleep(1)
        if n == 0:
            return 1
        else:
            return 'woot'

    result, runtime = example_func(10)
    print('result', result)
    print('runtime', runtime)
