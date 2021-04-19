def divide(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("Can't divide by zero!")


g_dividend, g_divider = input("Please enter devidend and devider separated by space >>> ").split()
# ^ Takes 2 arguments as a string and splits them by space symbol
print(divide(int(g_dividend), int(g_divider)))
# ^ Print result of divide function. Takes 2 arguments which being converted from str to int before passing to function
