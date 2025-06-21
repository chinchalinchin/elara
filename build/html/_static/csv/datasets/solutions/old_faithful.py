import csv, os, sys

import matplotlib.pyplot as plot

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

(fig, axs) = plot.subplots()

# read in data
with open(f'{data_directory}/old_faithful_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]

print(headers)
print(columns[:3])

eruptions = [ float(obs[0]) for obs in columns ]
waiting = [ float(obs[1]) for obs in columns ]

plot.title("Old Faithful Eruption Length (min) vs Waiting Time (min)")

axs.scatter(eruptions, waiting)
axs.set_xlabel("Eruption Length (Minutes)")
axs.set_ylabel("Waiting Time Until Next Eruption (Minutes)")

plot.show()