seasons = (
    "Winter",
    "Winter",
    "Spring",
    "Spring",
    "Spring",
    "Summer",
    "Summer",
    "Summer",
    "Autumn",
    "Autumn",
    "Autumn",
    "Winter"
)
try:
    print(seasons[int(input("Please enter month nimber (1-12) >>> ")) - 1])
    # Using input right in index field.                               ^ Deducting entered value to match index of list
except:
    print("Invalid month number!")
