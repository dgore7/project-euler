# Problem 6

def sum_of_squares(bound):
    result = 0
    for i in range(1, bound + 1):
        result += i * i
    return result

def square_of_sum(bound):
    result = sum(range(1, bound + 1))
    return result * result

if __name__ == '__main__':
    result = square_of_sum(100) - sum_of_squares(100)
    print(result)