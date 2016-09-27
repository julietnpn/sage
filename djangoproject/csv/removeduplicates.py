import csv

# with open('usda.orange.nogenusonly.csv', "r") as csvfile:
# 	with open('usda.orange.for_import.csv', 'w') as csvwritefile:

with open('CYBERSEES_InitialPlantList.csv', "r") as csvfile:
	with open('CYBERSEES_for_import.csv', 'w') as csvwritefile:
		lines_seen = set() # holds lines already seen
		
		for line in csvfile:
			if line not in lines_seen: # not a duplicate
				csvwritefile.write(line)
				lines_seen.add(line)
			else:
				print "duplicate"
		csvwritefile.close()