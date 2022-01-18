date = '2022-01-17'
year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])

print('Next class will be on', day + 1, '-', month, '-', str(year) + '.') 

def compute_tomorrow(data):
	year = data[0:4]
	month = data[5:7]
	day = int(data[8:10])
	return 'Tomorrow: ' + year + '-' + month + '-' + str(day + 1)

print(compute_tomorrow('2022-01-17'))