# Problem 7
import math


def sieve(target):
    marked = [False for i in range(10000000)]
    i = 2
    while i < math.sqrt(10000000):
        if not marked[i]:
            for m in range(i*2, 10000000, i):
                marked[m] = True
        i += 1
    count = 0
    for iteration in range(2, 10000000):
        if not marked[iteration]:
            count += 1
        if count == target:
            return iteration
    return -1

if __name__ == '__main__':
    print(sieve(10001))