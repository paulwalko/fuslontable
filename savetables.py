#!/usr/bin/env python3

import os
import sys
import time

import requests

tables = []
with open('tables.txt') as f:
    tables = f.readlines()
tables = [i.strip() for i in tables]


existing_data = os.listdir('./data')
count = 0
for table in tables:
    print("COUNT: {}".format(count))
    count += 1

    data_html = "{}.html".format(table)

    if data_html in existing_data:
        continue

    
    r = requests.get("https://fusiontables.googleusercontent.com/embedviz?q=select+*+from+{}&viz=CARD".format(table))
    while r.status_code == 429:
        print('Too Many Requests! :(')
        time.sleep(10 * 60)

        r = requests.get("https://fusiontables.googleusercontent.com/embedviz?q=select+*+from+{}&viz=CARD".format(table))

    if r.status_code != 200:
        print("Unexpected Code: {}".format(r.status_code))

    print("Saving ./data/{}".format(data_html))
    with open("./data/{}".format(data_html), 'w') as f:
        f.write(r.text)
