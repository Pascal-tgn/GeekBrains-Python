def prepend_by_zero(time):
    if time < 10:
        time = "0" + str(time)
    return time
seconds_total = int(input("Please enter time in seconds:"))
seconds = prepend_by_zero(seconds_total % 60)
minutes = prepend_by_zero((seconds_total // 60) % 60)
hours = prepend_by_zero((seconds_total // 60) // 60)
print("{}:{}:{}".format(hours, minutes, seconds))
