import os


import pandas as pd
import csv

plan_data = []
with open('plans.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        plan_data.append(row)
plan_data = pd.DataFrame(plan_data)
plan_data = plan_data[plan_data.metal_level == 'Silver'].sort_values(['rate_area', 'state'])

zipcode_data = []
with open('zips.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        zipcode_data.append(row)
zipcode_data = pd.DataFrame(zipcode_data)
zipcode_data = zipcode_data.sort_values(['rate_area', 'state'])

print('done')
