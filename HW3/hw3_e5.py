total = 0
continue_code = True
while continue_code:
    values = (input("Please enter values separated by space. Enter ; to stop >>>").split())
    for i in range(0, len(values)):
        if values[i] == ';':
            continue_code = False
            break
        else:
            total += int(values[i])
print(total)
