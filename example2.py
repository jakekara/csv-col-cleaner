'''
  example2.py
  by Jake Kara
  jkara@trendct.org

  Simple command line tool for replacing town names 
  in a spreadsheet

'''

import sys, ctclean

if len(sys.argv) < 5:
    print "Usage: %s in_col out_col in_file out_file" % sys.argv[0]
    exit (2)

print ctclean.ct_clean_file(sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4], error="Wah, wahh")
