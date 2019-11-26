#!/usr/bin/env python3

import os

import requests

tables = []
with open('tables.txt') as f:
    tables = f.readlines()
tables = [i.strip() for i in tables]

tables_error = []
with open('tables_error.txt') as f:
    tables_error = f.readlines()
tables_error = [i.strip() for i in tables_error]


existing_data = os.listdir('./data')
for table in tables:
    data_file = "{}.zip".format(table)

    if table in tables_error or data_file in existing_data:
        continue

    r = requests.get("https://fusiontables.googleusercontent.com/exporttable?query=select+*+from+{}&o=zip".format(table))
    print(r.status_code)
    if r.status_code != 200:
        print("Saving ./data/{}".format(data_file))
        with open("./data/{}".format(data_file), 'wb') as f:
            f.write(r.content)
    else:
        print("Adding {} to tables_error.txt".format(table))
        with open('./tables_error.txt', 'a') as f:
            f.write("{}\n".format(table))
