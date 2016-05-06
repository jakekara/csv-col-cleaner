# CT Name Cleaner, Python Edition
by Jake Kara
jkara@trendct.org



(With a handy module for generalizing lookup to other data sets)

### Files

1. example.py - Simple command line util for translating a ct town or village name to the proper town name, such as New Preston to Washington. Example usage:

    $ python example.py New\ Preston
    WASHINGTON

2. example2.py - Command line util for generating a CSV file with a new column for cleaned up names. Example usage:

    $ python example2.py Town Town_clean sample_data/Abuse\ report\ -\ For\ JSON.csv sample_data/output.csv

3. ctclean.py - Module for cleaning ct village names

4. replacer.py - Generalized class for looking up key values in a spreadsheet. The same technique useful for cleaning town names could be used for retrieving other commmon values, like town population.

### CT Name Cleaner
This is a python implementation of Andrew Ba Tran's R-based CT Name cleaner. Database of CT names maintained by Andrew Ba Tran and Trend CT.