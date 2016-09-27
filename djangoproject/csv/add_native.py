import csv

def inNative(row_usda):
	with open('cal_native.csv', "r") as calnative_csvreadfile:
		reader_native = csv.DictReader(calnative_csvreadfile)
		
		for row_native in reader_native:
			str_usda = row_usda['Scientific Name']
			str_native = row_native['Species']
			
			if str_usda == str_native:
				return True
			elif min(str_usda, str_native) is str_usda:
				return False
		return False

with open('plantlistformining.csv', "r") as usda_csvreadfile:
		with open('plantlistformining.natives.csv', 'w') as usda_csvwritefile:
		
			reader_usda = csv.DictReader(usda_csvreadfile)
			
			headers_usda = reader_usda.fieldnames
			headers_usda.append('ca native')
			writer= csv.DictWriter(usda_csvwritefile, headers_usda)
			writer.writeheader()
			
			for row_usda in reader_usda:
				if inNative(row_usda):
					row_usda['ca native'] = True
					writer.writerow(row_usda)
					print row_usda['Scientific Name']
				else:
					row_usda['ca native'] = False
					writer.writerow(row_usda)


