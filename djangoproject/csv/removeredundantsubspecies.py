import csv

with open('usda.norepeat.nogenusonly.csv', "r") as csvfile:
	with open('usda.norepeat.nogenusonly.noredundantspp.csv', 'w') as csvwritefile:		
		reader = csv.DictReader(csvfile)
		headers = reader.fieldnames
		writer= csv.DictWriter(csvwritefile, headers)
		writer.writeheader()
		for row in reader:
			str = row['Scientific Name']
			splitstr = str.split()
			if len(splitstr) == 4:
				 #writer.writerow(row)
				 #print row['Scientific Name']
				 #print(splitstr[2], splitstr[3])
				 if splitstr [1] == splitstr [3]:
				 	print row['Scientific Name']
				 	
#writer.close()
		#
		#	splitstr = str.split()
		#	for row2 in  splitstr:
		#		print row2
			#if splitstr[1] in splitstr[3]:
				#print row

