import random
my_filename = r'e5_datafile.txt'
with open(my_filename, 'w') as my_write_file:
    for i in range(10):
        my_write_file.write(f"{str(random.randint(10, 50))} ")
with open(my_filename, 'r') as my_read_file:
    numbers = my_read_file.readline().split()
    total = 0
    for number in numbers:
        total += int(number)
print(f"Sum of all numbers in file is: {total}")