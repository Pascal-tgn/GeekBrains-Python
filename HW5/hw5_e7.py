import json

source_file = r'e7_companies.txt'
out_file = r'e7_json_output.txt'
final_output = list()
companies = dict()
average_profit = dict()
counter = 0
total_profit = 0
with open(source_file, 'r') as companies_source:
    while True:
        line = companies_source.readline()
        if not line:
            break
        company_name, company_type, revenue, expenses = line.split()
        profit = int(revenue) - int(expenses)
        total_profit += profit
        counter += 1
        companies.update({company_name: profit})
final_output.append(companies)
average_profit.update({"Average profit": round((total_profit / counter), 2)})
final_output.append(average_profit)
with open(out_file, 'w') as output_file:
    json.dump(final_output, output_file)
