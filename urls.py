import csv
with open('urls.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
