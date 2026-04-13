import csv, os, sys

import matplotlib.pyplot as plot

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

(fig, axs) = plot.subplots(1, 2)

# read in data
with open(f'{data_directory}/earth_density_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]
    
# grab first column from csv file
column_1 = [ float(row[0]) for row in columns ]

print(column_1)

axs[0].hist(column_1, bins=8)
axs[1].boxplot(column_1, vert=False, whis=(0,100))

plot.show()
