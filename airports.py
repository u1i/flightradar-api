import sys
sys.getdefaultencoding()
# coding=utf-8

import flightradar24
fr = flightradar24.Api()
airports = fr.get_airports()

#print (airports.encode('utf-8'))

for row in airports["rows"]:

	# aname=row["name"].decode('ascii').encode('utf8')

	# print (row["iata"], row["country"], row["name"])
	print(row)
