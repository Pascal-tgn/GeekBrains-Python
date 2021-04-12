base_km = int(input("Please enter 1st day distance:"))
target_km = int(input("Please enter target distance:"))
days = 1
if target_km > base_km:
    while base_km < target_km:
        days += 1
        base_km += base_km/10
print("With 10% daily increase it will take {} days to reach the target".format(days))
