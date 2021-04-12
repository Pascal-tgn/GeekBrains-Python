number = input("Please enter a number:")
top_digit = 0
while len(number) > 0:
    check_digit=int(number[-1])
    if check_digit > top_digit:
        top_digit = check_digit
    number = number[:-1]
print("Maximum digit of entered number is:",top_digit)
