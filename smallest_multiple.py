# Problem 5


def divisible_by_range(number, bound):
    for i in range(2, bound):
        if number % i != 0:
            return False
    return True


def smallest_multiple():
    i = 20
    while not divisible_by_range(i, 20):
        i += 20
    return i

if __name__ == '__main__':
    print(smallest_multiple())