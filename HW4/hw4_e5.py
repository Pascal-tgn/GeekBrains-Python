from functools import reduce

source_numbers = [x for x in range(100, 1001) if x % 2 == 0]


def my_multiply(m1, m2):
    return m1 * m2


def my_sum(s1, s2):
    return s1 + s2


print("Multiplication of all elements is: ", reduce(my_multiply, source_numbers))
print("Sum of all elements is: ", reduce(my_sum, source_numbers))
