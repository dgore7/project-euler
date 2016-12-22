# Problem 3

import math

def largest_prime_factor(number):
    largest_prime = 2
    while number % 2 == 0:
        number = number // 2
    for i in range(3, int(math.sqrt(number)), 2):
        if number % i == 0:
            largest_prime = i
            while number % i == 0:
                number //= i
    return largest_prime

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))