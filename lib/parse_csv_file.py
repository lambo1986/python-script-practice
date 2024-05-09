import csv 

def parse_csv(file_path):
  with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      print(row['Name'], row['Email'], row['Phone'])

file_path = "./resources/data1.csv"
parse_csv(file_path)