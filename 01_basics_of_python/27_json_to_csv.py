import json
import csv

csv_file = open('states_csv.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Abbr', 'Area_codes'])

# get all the data in the file
with open('states.json') as f:
    json_data = json.load(f)