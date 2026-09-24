import openpyxl

"""import csv
with open('data.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
    writer.writerow(['Charlie', 35, 'Chicago'])
print("CSV file created successfully.")"""

data = [
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Data Summary"
header = ["Name", "Age", "City"]
ws.append(header)
for row in data:
    ws.append(row)

wb.save("data_summary.xlsx")
print("Excel file created successfully.")
    ws.append(row)
