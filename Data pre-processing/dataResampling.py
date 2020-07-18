#import libraries
import pandas as pd
import glob
import os

#directory path
path = 'E:/Research Workspace/Load-Forecasting/Dataset/PRECON'
allFiles = glob.glob(path + '/*.csv')

#Read CSV and resample timestamp to 1H
for filename in allFiles:
	df = pd.read_csv(filename, parse_dates=['Date_Time']).resample('1H', on='Date_Time').mean()
	#export to csv
	df.to_csv( filename, index=True, encoding='utf-8-sig')
