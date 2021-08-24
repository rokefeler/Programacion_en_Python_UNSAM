import csv
# f = open('Data/camion.csv')
# rows = csv.reader(f)
# headers = next(rows)
# print(headers)
# for row in rows:
#     print(row)
# f.close()


with open('Data/camion.csv') as f: 
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    for row in rows:
        print(row)

    