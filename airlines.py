import sys
sys.getdefaultencoding()
# coding=utf-8

import flightradar24
fr = flightradar24.Api()
airlines = fr.get_airlines()

for row in airlines["rows"]:

	# aname=row["name"].decode('ascii').encode('utf8')

	# print (row["iata"], row["country"], row["name"])
	print(row)
