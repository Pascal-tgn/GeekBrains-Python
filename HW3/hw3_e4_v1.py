def my_func(x, y):
    return x ** y


number = float(input("Please enter a real positive number >>>"))
power = int(input("Please enter natural negative power of number >>>"))
print(f"{power} power of {number} is: ", my_func(number, power))
