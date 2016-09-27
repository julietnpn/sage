import csv

with open('usda.orange.original.csv', "r") as csvfile:
	with open('usda.orange.nogenusonly.csv', 'w') as csvwritefile:
		#re = csv.reader(csvfile)
		#headers = re.next()
		
		reader = csv.DictReader(csvfile)
		headers = reader.fieldnames
		writer= csv.DictWriter(csvwritefile, headers)
		writer.writeheader()
		for row in reader:
			str = row['Scientific Name']
			splitstr = str.split()
			if len(splitstr) != 1:
				 writer.writerow(row)
				 print row['Scientific Name']

