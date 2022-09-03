import csv
import json

# Reading variables
fieldnames = ['id', 'track_name', 'price', 'prime_genre']

# reading csv file
with open('AppleStore.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for row in csv_reader:

        # Print list specified by columns
        print(
            f"{row['id']} | {row['track_name']} | {row['price']} | {row['prime_genre']}")

# Reading variables json
track_name = []

# reading json file
f = open('applestore.json',)
data = json.load(f)

# Make a loop in the specified column
for i in data:
    track_name.append(tuple(i.values()))

f.close()
# Print specified by columns
print(track_name)

