import csv


with open('contacts.csv') as contact_file:
    csv_reader = csv.reader(contact_file, delimiter=',')
    csv_reader.__next__() # skip headers of csv file
    for row in csv_reader:
        print(f'Name: {row[0]} Number: {row[1]}')
