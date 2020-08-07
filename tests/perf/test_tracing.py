import logging as log
import time

from src.pypper.perf.tracing import perf, profiling


def test_perf_tracing():
    @perf
    class MyClass:
        def __init__(self, name="Test"):
            self.name = name

        def do_things(self):
            time.sleep(0.001)
            log.info(f"{self.name} doing things...")

    obj = MyClass()
    obj.do_things()


def test_profiling_function():
    @profiling
    def do_things():
        pass

    do_things()


def test_exception_handling():
    ouch = None

    @profiling
    def do_things():
        raise ValueError

    try:
        do_things()
    except ValueError as e:
        log.info("successfully handled exception: %s", e)
        ouch = True

    assert ouch


def test_double_decorator():
    @perf
    class MyClass:
        def __init__(self, name="Test"):
            self.name = name

        @profiling
        def do_things(self):
            log.info(f"{self.name} doing things...")

    obj = MyClass()
    obj.do_things()
