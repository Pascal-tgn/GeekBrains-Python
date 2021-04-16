seasons = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}
try:
    print(seasons.get(int(input("Please enter month nimber (1-12) >>> "))))
    # Using input right in key field.
except:
    print("Invalid month number!")
