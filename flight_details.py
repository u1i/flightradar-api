import sys
sys.getdefaultencoding()
# coding=utf-8

import flightradar24

flight = 'SQ212'
fr = flightradar24.Api()
details = fr.get_flight(flight)

print (details)

