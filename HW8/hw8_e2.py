class ZeroDev(Exception):
    def __init__(self, text):
        self.text = text


a, b = input("Please enter 2 nimber separated by space >>> ").split()
try:
    result = int(a) / int(b)
    print(result)
except ZeroDivisionError:
    print(ZeroDev("Zero division exception. 2nd value should not be zero!"))