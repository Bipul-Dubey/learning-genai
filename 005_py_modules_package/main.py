from math import sqrt, factorial
print(sqrt(4), factorial(5))


import os

print(os.getcwd(),"\n", os.getcwdb())


# packages
from packages.maths import Addition, substraction
print(Addition(3,4), substraction(10, 4))


# import shutil
# shutil.copy("source.txt","destination.txt")

# json
import json
data={"name":"Bipul", "age": 26}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))


parsed_Data = json.loads(json_str)
print(parsed_Data)
print(type(parsed_Data))

# csv
import csv

with open("example.csv",mode="w", newline="") as file:
    writer = csv.writer(file)
    # writer.writerow(["name", "age"])
    # writer.writerow(["Bipul", "32"])
    # writer.writerow(["Rehul", "33"])
    writer.writerows([["name", "age"],["Bipul", "32"],["Rehul", "33"]])

with open("example.csv",mode="r") as file:
    rows = csv.reader(file)
    for r in rows:
        print(r)
