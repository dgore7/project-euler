# Problem 4

def largest_palindrome_product_of_3_digits():
    largest = 0
    for a in reversed(range(100, 1000)):
        for b in reversed(range(100, 1000)):
            if is_palindromic_number(a*b):
                largest = max(largest, a * b)
    return largest

def is_palindromic_number(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    left = 0
    right = len(digits)-1
    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(largest_palindrome_product_of_3_digits())