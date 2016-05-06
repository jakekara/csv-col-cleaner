'''
  example.py
  by Jake Kara
  jkara@trendct.org

  Simple command line tool for getting the proper town name from a village or catalogued misspelling.

'''

import sys, ctclean

if len(sys.argv) < 2:
    print "Usage: %s town_name" % sys.argv[0]
    exit (2)

print ctclean.ct_clean(sys.argv[1], error="Wah, wahh")
