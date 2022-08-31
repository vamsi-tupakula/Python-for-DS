import json
import csv

# get all the data in the file
with open('states.json') as f:
    json_data = json.load(f)