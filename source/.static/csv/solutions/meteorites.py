"""
Skewed Right
"""

import csv, os, sys

import matplotlib.pyplot as plot


def divider():
	print("-----------------------------------------------------")
	
# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

(fig, axes) = plot.subplots()

# read in data
with open(f'{data_directory}/meteorite_landings_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
data = raw_data[1:]

print("------------ Meteorite Landings ---------------------")
print("Variables :", headers)
divider()

# empty masses!
mass = [ float(obs[4]) for obs in data if obs[4] != '' ]
  
min_mass = min(mass)
max_mass = max(mass)
mass_range = max_mass - min_mass 
inc = 20
step = mass_range/inc

bins = [ min_mass + (i+1)*step for i in range(inc) ]
print("maximum mass: ", min_mass)
print("minimum mass: ", max_mass)
divider()

axes.hist(mass, bins=bins)

plot.show()
