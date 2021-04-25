def my_factorial(f):
    my_total = 1
    for number in range(1, f + 1):
        my_total *= number
        yield my_total
    if my_total == 0:
        my_total = 1
        yield my_total


my_count = int(input("Please enter a number >>> "))
my_results = my_factorial(my_count)
n = 1
for i in my_factorial(my_count):
    print(f"{n}! = {i}")
    n += 1
