"""
Simple context timer for profiling (demo use only).
"""
import time
from contextlib import contextmanager

@contextmanager
def timer(name: str):
    start = time.time()
    yield
    end = time.time()
    print(f"[TIMER] {name}: {end - start:.3f}s")
