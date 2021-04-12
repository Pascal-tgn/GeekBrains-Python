revenue = int(input("Please enter annual revenue:"))
expences = int(input("Please enter annual expences:"))
if revenue > expences:
    profit = revenue - expences
    print("Profit: revenue is more than expences! Profit coefficient is:",profit / revenue)
    personnel = int(input("How many employees works in your company?"))
    print("Profit per person is: %.2f" % (profit / personnel))
else:
    print("Last annual period closed with no profit")
