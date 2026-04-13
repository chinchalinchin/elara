

import csv, os, sys

import matplotlib as mpl

import matplotlib.pyplot as plt

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

# read in data
with open(f'{data_directory}/electric_vehicle_population_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]

print(raw_data[0])
columns = raw_data[1:]

n = len(columns)

make = [ row[6] for row in columns ]
veh_type = [ row[8] for row in columns ]
make_and_type = [ (row[6], row[8]) for row in columns ]
eligibility = [row[9] for row in columns ]
veh_and_elig = [ (row[8], row[9]) for row in columns ]

print(make[:5])

freq_of_tesla = sum(1 for obs in make if obs == "TESLA")

print(freq_of_tesla)











plt.show()
