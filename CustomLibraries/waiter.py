import time as t
from typing import Literal

def wait(time):
    t.sleep(time)

def clock_info(name: Literal['monotonic', 'perf_counter', 'process_time', 'time', 'thread-time']):
    t.get_clock_info()