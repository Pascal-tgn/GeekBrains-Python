user_list = list(input("Please enter something >>>"))
print("Original list:", user_list)
i = 0
while (i + 1) < len(user_list):
    if (user_list[i + 1]) != None:
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i += 2
print("Modified list:", user_list)
