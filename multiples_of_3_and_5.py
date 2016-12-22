# Problem 1


def sum_multiples_of_3_and_5(bound):
    result = 0
    for i in range(bound):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

if __name__ == '__main__':
    print(sum_multiples_of_3_and_5(1000))