# Problem 2

def fib_gen(bound):
    prev = 1
    current = 1
    while current < bound:
        temp = current
        current = current + prev
        prev = temp
        yield current


if __name__ == '__main__':
    result = 0
    for i in fib_gen(4000000):
        if i % 2 == 0:
            result += i

    print(result)