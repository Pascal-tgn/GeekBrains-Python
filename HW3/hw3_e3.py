def my_func(arg1, arg2, arg3):
    """
    Function takes 3 arguments, converts them to int and sorts descending.
    :return: sum of first two arguments.
    """
    values = sorted([int(arg1), int(arg2), int(arg3)], reverse=True)
    print(f"Max possible sum is: {values[0]+values[1]}\nIt can be achieved by adding {values[1]} to {values[0]}.")


value1, value2, value3 = input("Please enter 3 values separated by space >>> ").split()
my_func(arg1=value1, arg2=value2, arg3=value3)
