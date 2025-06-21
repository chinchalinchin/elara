import csv, os, sys

import matplotlib

matplotlib.use('tkagg')

import matplotlib.pyplot as plt

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

fig, axs = plt.subplots()
# fig, axs = plt.subplots(1, 4)

# read in data
with open(f'{data_directory}/vietnam_draft_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]
    
# grab first column from csv file
column_1 = [ float(row[0]) if row[0].isnumeric() else 0 for row in columns ]
column_2 = [ float(row[1]) if row[1].isnumeric() else 0 for row in columns ]
column_3 = [ float(row[2]) if row[2].isnumeric() else 0 for row in columns ]
column_4 = [ float(row[3]) if row[3].isnumeric() else 0 for row in columns ]
column_5 = [ float(row[4]) if row[4].isnumeric() else 0 for row in columns ]
column_6 = [ float(row[5]) if row[5].isnumeric() else 0 for row in columns ]

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

data_1969 = [ 0 ] * 12
data_1970 = [ 0 ] * 12
data_1971 = [ 0 ] * 12
data_1972 = [ 0 ] * 12

for index, entry in enumerate(column_1):
    data_1969[int(entry) - 1] += column_3[index]
    data_1970[int(entry) - 1] += column_4[index]
    data_1971[int(entry) - 1] += column_5[index]
    data_1972[int(entry) - 1] += column_6[index]

axs.bar(months, data_1969, width=1)

# axs[0].bar(months, data_1969, width=1)
# axs[1].bar(months, data_1970, width=1)
# axs[2].bar(months, data_1971, width=1)
# axs[3].bar(months, data_1972, width=1)
plt.show()