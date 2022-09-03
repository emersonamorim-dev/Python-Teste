import csv

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
