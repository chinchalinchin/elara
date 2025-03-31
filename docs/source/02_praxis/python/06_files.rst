.. _files:

=====
Files
=====

.. _csv_files:

CSV Files
=========

The ``csv`` package gives us a way to load in data from an external ``.csv`` file. The following example will load in a ``.csv`` file named ``example.csv``, assuming the ``.csv`` file is saved in the same folder (directory) as the ``.py`` script.

.. important:: 
    
    This example will only work if the script ``.py`` file is saved in the same directory as the data ``.csv`` file.

.. code-block:: python 

    import csv

    # read in data
    with open(f'example.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        raw_data = [ row for row in csv_reader ]

    # separate headers from data
    headers = raw_data[0]
    columns = raw_data[1:]

    # grab first column from csv file and ensure it's a number (not a string)
    column_1 = [ float(row[0]) for row in columns ]

    print(column_1)