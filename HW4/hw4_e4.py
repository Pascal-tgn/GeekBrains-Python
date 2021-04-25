from random import randint
my_numbers = [randint(1, 10) for x in range(20)]
unique_numbers = []
print(my_numbers)
for number in my_numbers:
    if my_numbers.count(number) == 1:
        unique_numbers.append(number)
print(unique_numbers)
