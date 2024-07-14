import csv

with open('csv_file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Shubham', '21', 'Pune'])
    writer.writerow(['Raj', '22', 'Mumbai'])
    writer.writerow(['Ram', '23', 'Nagpur'])


with open('csv_file.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        print(row)
