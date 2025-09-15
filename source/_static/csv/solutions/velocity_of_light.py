import csv, os, sys

import matplotlib.pyplot as plot
import statistics as stat

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

(fig, axs) = plot.subplots(2)

# read in data
with open(f'{data_directory}/velocity_of_light_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]
    
# grab first column from csv file
column_1 = [ float(row[0]) for row in columns ]

n = len(column_1)
classes = 10
sample_mean = stat.mean(column_1)
sample_min = min(column_1)
sample_max = max(column_1)
sample_range = sample_max - sample_min
sample_stdev = stat.stdev(column_1)
quartiles = stat.quantiles(column_1, n=4)
percentiles = stat.quantiles(column_1, n=100)
class_width = sample_range / classes

ideal_dist = stat.NormalDist(sample_mean, sample_stdev)

ticks = [ sample_min + i * class_width for i in range(classes + 1) ]
ideal = [ ideal_dist.pdf(x) for x in ticks ]

plot.suptitle(f"Velocity of Light \n n = {n}")
axs[0].hist(column_1, bins=ticks, density=True, color="lightblue", ec="red")
axs[0].set_xticks(ticks)
axs[0].set_ylabel("Freq (%)")
axs[0].plot(ticks, ideal, color="purple")
axs[1].boxplot(column_1, vert=False, whis=(0,100))
axs[1].set_xticks(ticks)
axs[1].set_xlabel("km/s")

plot.show()
