#WAP to read data from CSV file and convert the data to JSON format. Write the JSON to .json output file.
import csv
import json
csv_file_path = "input.csv"
json_file_path= "output.json"

with open (csv_file_path,mode="r",encoding="utf-8") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    data=list(csv_reader)
with open (json_file_path,mode="w",encoding="utf-8") as json_file:
    json.dump(data,json_file,indent=4)