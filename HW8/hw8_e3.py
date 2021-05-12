class CustomExceptions:
    numbers = []

    def __init__(self):
        while True:
            number = input("Please enter a number. Enter 'stop' to finish >>> ")
            if number.isdigit():
                self.numbers.append(number)
            elif number.lower() == 'stop':
                print(f"All numbers entered: {self.numbers}")
                break
            else:
                print("Not a number. Please enter integer data.")


CustomExceptions()
