# load all data
dataset = read_csv('swedenLoadData.csv', low_memory=False, infer_datetime_format=True, parse_dates={'datetime':[0,1]}, index_col=['datetime'])

# mark all missing values
dataset.replace('?', nan, inplace=True)

# make dataset numeric
dataset = dataset.astype('float32')

# fill missing values with a value at the same time one day ago
def fill_missing(values):
	one_day = 60 * 24
	for row in range(values.shape[0]):
		for col in range(values.shape[1]):
			if isnan(values[row, col]):
				values[row, col] = values[row - one_day, col]
# fill missing
fill_missing(dataset.values)