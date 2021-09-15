from functools import partial, wraps
import os
from subprocess import check_output

run = partial(check_output, encoding='utf-8')

def path2str(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        args = [str(a) for a in args]
        return f(*args, **kwargs)
    return wrapper

@path2str
def invisible(f):
    for s in f.split(os.sep):
        if s.startswith('.'):
            return True
    return False
