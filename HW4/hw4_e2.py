from random import randint


class DoColors:
    GREEN = '\033[92m'
    END = '\033[0m'


def highlight_and_select(num, color, position, maximum):
    """
    Prints putput with highlighted selected numbers
    :param num: current number
    :param color: True if number selected
    :param position: Position of current number
    :param maximum: total amount of numbers
    :return: none
    """
    if color:
        print(f"{DoColors.GREEN}{num}{DoColors.END}", end='')
        filtered_numbers.append(my_numbers[number])
    else:
        print(f"{num}", end='')
    if position < maximum - 1:
        print(", ", end='')
    else:
        print(end=f"]\n")


# Generate random sequence, from 10 to 20 elements
my_numbers = [randint(1, 100) for x in range(randint(10, 20))]
filtered_numbers = []
colored_numbers = []
print(f"Original sequence: {my_numbers}")
print("Highlight:         [", end='')
for number in range(0, len(my_numbers)):
    highlight_and_select(
        my_numbers[number],
        # Returns True if element is higher than previous one
        (my_numbers[number] > my_numbers[number - 1]) & (number > 0),
        number,
        len(my_numbers)
    )
print("\nFiltered selection: ", filtered_numbers)
