import sys
sys.getdefaultencoding()
# coding=utf-8

import flightradar24

airline = 'SIA'
fr = flightradar24.Api()
flights = fr.get_flights(airline)

print (flights)

#for key,value in flights.items():

#	print(key, value)
