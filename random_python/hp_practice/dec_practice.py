import numpy as np
import time

def timing_function(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper

def sleep_function(f):
    def wrapper():
        f()
        time.sleep(10)
        return 'Time waited'

    return wrapper

def check_input(*types):
    def check_acceps(f):
        assert len(types) == f.func_code.co_argcount
        def new_f(*args, **kwds):
            for (a,t) in zip(args, types):
                assert isinstance(a, t),  \ 
                   f 'arg %{a} does not match t}" % (a,t)'

@timing_function
@sleep_function
def some_function():
    print('Some function acting here!')

print(some_function())

