import logging as log
import sys
import time
import types
from functools import wraps

root = log.getLogger()
root.setLevel(log.DEBUG)

handler = log.StreamHandler(sys.stdout)
handler.setLevel(log.DEBUG)
formatter = log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

__trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType
)


def profiling(func):
    if hasattr(func, "tracing"):
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            end = time.time()
            log.debug(f"{func.__name__}() took {(end - start) * 1000.0:.3f} ms")

    wrapper.tracing = True
    return wrapper


def perf(klass):
    for key in dir(klass):
        member = getattr(klass, key)
        if isinstance(member, __trace_types):
            wrapped = profiling(member)
            setattr(klass, key, wrapped)
    return klass
