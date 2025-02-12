import csv, os, sys

import matplotlib.pyplot as plot

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

(fig, axs) = plot.subplots()

# read in data
with open(f'{data_directory}/kentucky_derby_winners_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]

print(headers)
print(columns[:3])

year = [ int(obs[0]) for obs in columns ]
seconds = [ float(obs[8]) for obs in columns ]

axs.scatter(year, seconds)
axs.set_xlabel("Year")
axs.set_ylabel("Seconds")

plot.show()