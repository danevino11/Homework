import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    "Some weird voodoo magic calculations"
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(func, nums):
    with Pool(500) as p:
        return sum(p.map(func, nums))


if __name__ == "__main__":
    nums = [i for i in range(501)]
    print(fast(slow_calculate, nums))
    
