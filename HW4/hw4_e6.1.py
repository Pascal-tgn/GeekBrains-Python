from itertools import count

my_start = int(input("Please enter number to start from >>> "))
my_finish = int(input("Please enter maximum number to count to >>> "))
for n in count(my_start, 1):
    print(n)
    if n == my_finish:
        break
