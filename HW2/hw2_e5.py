ratings = [7, 5, 3, 3, 2]
repeat = "Y"
while repeat.upper() != "N":
    new_rating = int(input("Please enter a new rating to add >>> "))
    i = 0
    while i < len(ratings):
        if ratings[i] < new_rating:
            ratings.insert(i, new_rating)
            break
        i += 1
    if i == len(ratings):
        ratings.append(new_rating)   # If no elements is smaller - append rating to the end
    repeat = input("Do you want to add another one [Y/n]?")
print(ratings)
