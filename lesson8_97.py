import csv


with open('test.csv', 'w', newline='') as csv_file:
    filednames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=filednames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])