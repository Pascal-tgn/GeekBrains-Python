from itertools import cycle

my_list = [1, 3, 34, 6, 23, 324, 23, "q"]
print(f"Source list is: {my_list}")
my_finish = int(input("Please enter number or repeats >>> "))
my_counter = 0
cycled_list = []
for n in cycle(my_list):
    my_counter += 1
    cycled_list.append(n)
    if my_counter == my_finish * len(my_list):
        break
print(cycled_list)
