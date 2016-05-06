'''
CT Name Cleaner, python edition
By Jake Kara
jkara@trendct.org
Spreadsheet maintained by Andrew Ba Tran / Trend CT

Usage: import ctclean
       ctclean.clean_name("NEW PRESTON")
       returns: "WASHINGTON" or False if not found

Usage optional error parameter to override False ret
val. For instance:

       ctclean.clean_name(town_var, error=town_var)

Will just fall back to the town name supplied if not
found in the spreadsheet
'''


import replacer

__csv_url = "https://docs.google.com/spreadsheets/d/1WqZIGk2AkHXKYvd4uXy5a2nwyg529e7mMU5610Ale0g/pub?gid=0&single=true&output=csv"

__town_cleaner = replacer.Replacer(__csv_url,
                                 "name",
                                 "real.town.name")

# Wrapper for replacer function
ct_clean = __town_cleaner.replace

ct_clean_file = __town_cleaner.replace_in_file
