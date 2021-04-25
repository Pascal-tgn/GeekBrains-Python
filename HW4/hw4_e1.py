from sys import argv

script_name, hourly_rate, hours, bonus = argv
total = int(hourly_rate) * int(hours) + int(bonus)
print(f"Total amount to pay is: {total}")
