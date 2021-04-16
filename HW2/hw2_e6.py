store_items = [
    (1, {"Name": "Laptop", "Price": 950, "Quantity": 5, "Measure": "Piece(s)"}),
    (2, {"Name": "Monitor", "Price": 349, "Quantity": 11, "Measure": "Piece(s)"}),
    (3, {"Name": "Keyboard", "Price": 20, "Quantity": 20, "Measure": "Piece(s)"}),
    (4, {"Name": "Mouse", "Price": 17, "Quantity": 14, "Measure": "Piece(s)"}),
    (5, {"Name": "Printer", "Price": 150, "Quantity": 2, "Measure": "Piece(s)"}),
    (6, {"Name": "UTP Cable", "Price": 0.5, "Quantity": 500, "Measure": "Meter(s)"})
]
#for item in store_items:
i = 0
all_keys = list()
while len(store_items) > i:
    for key in store_items[i][1].keys():
        all_keys.append(key)
    i+=1
all_keys = list(set(all_keys))
final_result = list()
for keyname in all_keys:
    i = 0
    result = ''
    result = "{0}{1}".format(result, (keyname + ":"))
    while len(store_items) > i:
        value = (store_items[i][1].get(keyname))
        result = "{0} {1},".format(result, value)
        i += 1
#    print(result)
    final_result.append(result[:-1])
print(*final_result, sep="\n")
