import sys
import json
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]
output_fp = open(output_file, 'w', encoding='utf-8')

# Create the csv writer object
csv_writer = csv.writer(output_fp)

# Counter variable used for writing
# headers to the CSV file
count = 0

with open(input_file, 'r') as fp:
    for line in fp:
        user = json.loads(line) 
        if count == 0:
            # Writing headers of CSV file
            header = user.keys()
            csv_writer.writerow(header)
            count += 1
        # Writing data of CSV file
        csv_writer.writerow(user.values())

output_fp.close()
