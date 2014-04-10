import csv


def clean_up_data():
	# open the csv file
	print "Opening file..."
	myfile = open('data.csv', 'rb')

	# instantiate the csv module
	lines = csv.reader(myfile)

	# save the header for future reference and append 'result' column
	header = lines.next()
	header.append('result')
	header.append('from column')


	# create a big list for each line in the csv file
	# inefficient...but what the hell
	list_of_lines = []
	for line in lines:
	    list_of_lines.append(line)


	# assign the column indexes for the columns we care about
	pa1 = 11
	pa2 = 12
	ma1 = 6


	# iterate our big_list create above
	print "Parsing each csv line..."
	for a_line in list_of_lines:

		# get the value for corresponding column and strip preceeding/proceeding spaces
		pa1_str = a_line[pa1].strip()
		pa2_str = a_line[pa2].strip()
		ma1_str = a_line[ma1].strip()

		# return the correct address and append to list
		result = return_one(pa1_str, pa2_str, ma1_str)
		a_line.append(result[0])
		a_line.append(result[1])

	# add header row
	list_of_lines.insert(0, header)


	new_file = open('result.csv', 'wb')
	wr = csv.writer(new_file, quoting=csv.QUOTE_ALL)
	wr.writerows(list_of_lines)
	print "File creation complete..."
	print "Closing Files...Done..."
	new_file.close()
	myfile.close()
	
	return "Complete"


def return_one(pa1_str, pa2_str, ma1_str):
	if check_true(pa1_str) is True:
		return [pa1_str, 'pa1']


	if check_true(pa2_str) is True:
		return [pa2_str, 'pa2']


	if check_true(ma1_str) is True:
		return [ma1_str, 'ma1']

	return ['check manually', 'none']


def check_true(value):
	# checks to see if there is > one word in field
	if len(value.split(" ")) < 2:
		return False

	# checks if the first word begins with an '#' or '.' - if so; remove it
	if value.split(" ")[0][0] in ['#', '.']:
		value = value[1:]

	try:
		# checks if the string is an integer
		int(value.split(" ")[0])
		return True

	except ValueError:
		return False


# entry point for app
if __name__ == "__main__":
	print "Beginning Script..."
	clean_up_data()
